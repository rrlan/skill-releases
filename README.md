# rrlan Skill 发行包

源码在私有仓库维护，这里只提供发行包、版本索引和通用下载入口。下载和安装不需要 GitHub/GitLab 账号。

## 已发布 Skill 列表

| Skill 名称 | 最新版本 | 核心能力简介 | 一键安装 / 更新命令 |
|---|---|---|---|
| `pure-code-video` | `1.2.0` | 530+ 纯代码视频风格选片台、60fps 虚拟时钟渲染、手绘水彩引擎、12 款 BPM/Bit 节拍合成器、109 款 CC0 音效 `-16 LUFS` 混音、真人录音预剪/音色克隆/逐字字幕对齐（[在线选片与试听台](https://rrlan.github.io/pure-code-video/)） | `curl -fsSL https://raw.githubusercontent.com/rrlan/skill-releases/main/install.py -o /tmp/rrlan-skill-install.py && python3 /tmp/rrlan-skill-install.py pure-code-video` |
| `ip-library-factory` | `1.1.1` | 原创 IP 角色素材库工厂（身份锁定、三视图母版、低中高电量状态、透明 PNG 与社媒封面规范） | `curl -fsSL https://raw.githubusercontent.com/rrlan/skill-releases/main/install.py -o /tmp/rrlan-skill-install.py && python3 /tmp/rrlan-skill-install.py ip-library-factory` |

## 安装与更新

需要已有 Python 3.9+ 和 Node.js/npm，并能访问 GitHub、npm 和 Python 包下载源。

macOS / Linux：

```bash
curl -fsSL https://raw.githubusercontent.com/rrlan/skill-releases/main/install.py -o /tmp/rrlan-skill-install.py && python3 /tmp/rrlan-skill-install.py ip-library-factory
```

Windows PowerShell（未实机验收）：

```powershell
Invoke-WebRequest https://raw.githubusercontent.com/rrlan/skill-releases/main/install.py -OutFile "$env:TEMP\rrlan-skill-install.py"
py -3 "$env:TEMP\rrlan-skill-install.py" ip-library-factory
```

**更新时重复相同命令**，始终读取 catalog.json 中指定的稳定版本。不要使用包内 `install.py --update` 更新本渠道；该选项用于直接从 Git 仓库安装的用户。

默认安装到 Codex 个人范围；在 Python 命令后追加 `--project /path/to/project` 可改为项目范围。安装器会校验 ZIP 的 SHA-256，自动建立或复用外部 Python 环境、安装依赖并运行 doctor；无需手工激活虚拟环境。失败恢复由包内安装器完成。API Key、系统字体和 Python/Node 本身由使用者准备，安装不会调用付费 API。

## 本地安装包

从 Releases 下载 ZIP，解压后执行：

```bash
python3 ip-library-factory/install.py
```

收到新版 ZIP 后重复执行。回退也可运行历史版本 ZIP 的安装入口。

更新会替换 Skill 目录；自己的 IP 项目、照片、配置与作品应放在 Skill 目录外。包内 INSTALL.md 的“在线渠道”描述私有源码仓库直装；本公开发行渠道以本页为准。

## 维护约定

每个 Skill 使用独立 tag，例如 `ip-library-factory-v1.1.1`。发行包只包含运行所需文件，不带 Git 历史、凭据、作品或虚拟环境。先验证版本包，再上传对应 Release，最后更新 catalog.json 中该 Skill 的版本、地址、SHA-256 和来源 commit。其他 Skill 复用同一入口，包顶层目录与 Skill 名一致，提供自动准备依赖的 install.py。
