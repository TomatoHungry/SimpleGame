import os
import json
import subprocess

minecraft_dir = os.path.join(os.getcwd(), '.minecraft')
java_path = "java"
memory = "4G"

def launch_game(version, name):
    # 版本信息
    version_json_path = os.path.join(minecraft_dir, 'versions', version, f'{version}.json')
    with open(version_json_path, 'r', encoding='utf-8') as f:
        version_info = json.load(f)
    
    # 构建classpath
    libraries = []
    for lib in version_info['libraries']:
        lib_path = os.path.join(minecraft_dir, 'libraries', lib['downloads']['artifact']['path'])
        libraries.append(lib_path)
    libraries.append(os.path.join(minecraft_dir, 'versions', version, f'{version}.jar'))
    classpath = os.pathsep.join(libraries)

    # 构建启动命令
    command = [
        java_path,
        f'-Xmx{memory}',
        f'-Xms512M',
        f'-Djava.library.path={os.path.join(minecraft_dir, 'versions', version, "natives-windows-x86_64")}',
        '-cp', classpath,
        version_info['mainClass'],
        '--username', name,
        '--version', version,
        '--gameDir', minecraft_dir,
        '--assetsDir', os.path.join(minecraft_dir, 'assets'),
        '--accessToken', '0',
        '--userType', 'legacy',
        '--versionType', 'Zephyr'
    ]

    # 启动游戏
    print(f'启动 Minecraft {version}')
    print(f'用户名: {name}')
    print(f'java路径: {java_path}')
    print(f'游戏文件夹路径: {minecraft_dir}')
    print(f'内存: {memory}')
    print(f'版本: {version}')
    subprocess.run(command)

command = str(input('> ')).split(' ')

# 简单解析命令

if len(command) != 3:
    print('命令无效')
if command[0] == 'launch':
    launch_game(command[1], command[2])