from modules import recon, vuln_scan, exploit, persistence, report
from gpt_helper import ask_gpt
import time

def main():
    target = input("请输入目标 IP 或域名: ")

    print("\n[1] 信息收集阶段...")
    recon_data = recon.run_recon(target)
    print("\n由 GPT 分析信息收集结果：")
    print(ask_gpt(recon_data, "请分析此信息收集结果，识别潜在弱点与下一步建议。"))

    print("\n[2] 漏洞探测阶段...")
    scan_result = vuln_scan.run_scan(target)
    print("\n由 GPT 分析漏洞扫描结果：")
    print(ask_gpt(scan_result, "根据扫描结果列出可用漏洞或攻击点。"))

    print("\n[3] 漏洞利用阶段...")
    exploit_logs = exploit.run_exploit(target)
    print("\n由 GPT 分析攻击过程：")
    print(ask_gpt(exploit_logs, "分析攻击输出，判断是否成功利用，是否需要权限提升。"))

    print("\n[4] 权限维持阶段...")
    persistence_result = persistence.run_persistence(target)
    print("\nGPT 权限维持建议：")
    print(ask_gpt(persistence_result, "请总结权限维持结果并提出持续控制策略。"))

    print("\n[5] 渗透测试报告生成中...")
    report.generate_report(target, recon_data, scan_result, exploit_logs, persistence_result)

if __name__ == "__main__":
    main()
