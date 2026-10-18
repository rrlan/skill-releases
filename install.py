#!/usr/bin/env python3
"""Download a published Skill package and run its dependency-aware installer."""
import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tempfile
import urllib.request
import zipfile

CATALOG = 'https://raw.githubusercontent.com/rrlan/skill-releases/main/catalog.json'


def download(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'rrlan-skill-installer'})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def main():
    parser = argparse.ArgumentParser(description='安装或更新公开发行的 Skill，同时自动准备依赖。')
    parser.add_argument('skill', help='例如 ip-library-factory')
    parser.add_argument('--project', type=Path, help='安装到指定项目，默认 Codex 个人范围')
    parser.add_argument('--with-api', action='store_true', help='准备可选 API SDK，不调用 API')
    args = parser.parse_args()
    if sys.version_info < (3, 9):
        parser.error('需要 Python 3.9 或更新版本')
    catalog = json.loads(download(CATALOG))
    if args.skill not in catalog['skills']:
        parser.error('未找到该 Skill：' + args.skill)
    entry = catalog['skills'][args.skill]
    print('下载 {} {}…'.format(args.skill, entry['version']), flush=True)
    payload = download(entry['url'])
    if hashlib.sha256(payload).hexdigest() != entry['sha256']:
        raise RuntimeError('下载包校验失败，请重新执行安装命令。')
    with tempfile.TemporaryDirectory(prefix='rrlan-skill-release-') as folder:
        root = Path(folder)
        with zipfile.ZipFile(io.BytesIO(payload)) as archive:
            for member in archive.infolist():
                path = PurePosixPath(member.filename)
                if path.is_absolute() or '..' in path.parts or '\\' in member.filename:
                    raise RuntimeError('安装包包含无效路径')
            archive.extractall(root)
        installer = root / args.skill / 'install.py'
        if not installer.is_file():
            raise RuntimeError('安装包缺少 install.py')
        command = [sys.executable, str(installer)]
        if args.project:
            command += ['--project', str(args.project.expanduser().resolve())]
        if args.with_api:
            command += ['--with-api']
        subprocess.run(command, check=True)
    print('完成。以后重新执行相同下载与安装命令即可更新。')


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print('安装失败：' + str(error), file=sys.stderr)
        sys.exit(1)
