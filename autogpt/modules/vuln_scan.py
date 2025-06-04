import subprocess

def run_scan(target):
    cmd = f"nuclei -u {target} -silent"
    result = subprocess.getoutput(cmd)
    return f"[Nuclei 漏洞扫描结果]\n{result}"


#功能：使用 Nuclei 扫描漏洞，GPT 用于分析结果并提出利用建议
#可扩展：调用 CVE 数据库、Metasploit scanner、OpenVAS 等
