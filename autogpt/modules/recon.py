import subprocess

def run_recon(target):
    cmd = f"nmap -sV -Pn {target}"
    result = subprocess.getoutput(cmd)
    return f"[NMAP 扫描结果]\n{result}"


#功能：执行基础 Nmap 扫描（端口、服务版本）
#后续：结果传给 GPT 分析资产弱点和暴露面
