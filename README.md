中国象棋残局优化：
“蚯蚓降龙”是中国象棋残局中的一个典型对抗局面，常被用于分析复杂的战略博弈。
黑方依次采用随机走卒策略、启发式规则策略与基础MCTS策略进行模拟，红方则统一使用防守导向的启发式策略以控制胜率上限，从而实现三种基础策略（p₁、p₂、p₃）下的胜率对比评估。重点开展MCTS算法的多维度优化设计，涵盖UCB1-Tuned变体引导式搜索、动作合法性过滤、基于规则的快速模拟策略、等技术方案，形成优化树搜索策略（p₄）。经过500轮模拟对局验证，优化后的树搜索策略使红方的胜率从基础MCTS的41.4%提高到了52%。

爬虫：
爬取了豆瓣TOP250的电影排行

邮箱伪造漏洞：
该漏洞可以以别的学校的名义给指定用户发送邮件，若稍加利用可能会造成一定的影响。

autogpt:
外部工具：
工具名称         作用简述                        安装方式（Linux/macOS）            
`nmap`           端口扫描、服务识别              `sudo apt install nmap` / `brew install nmap`                       
`nuclei`         快速漏洞模板扫描                见(https://github.com/projectdiscovery/nuclei)        
`sqlmap`         SQL 注入自动化检测与利用        `sudo apt install sqlmap` 或 `pip install sqlmap`                     
`sublist3r`      子域枚举工具                    `pip install sublist3r`                                              
`amass`          子域名发现 + DNS 扫描           `snap install amass` 
`metasploit`     渗透测试框架，利用+后门部署支持  见[https://docs.metasploit.com/](https://docs.metasploit.com/)      
`netcat`         建立反弹 shell、监听端口等       `sudo apt install netcat`                                             
`empire`         后渗透控制平台（后门）           手动配置                                                 

项目目录：
PentestGPT/
├── main.py                         # 项目主控入口
├── config.py                       # 配置文件（API Key 等）
├── requirements.txt                # 所需依赖
├── modules/
│   ├── recon.py                    # 信息收集模块
│   ├── vuln_scan.py               # 漏洞探测模块
│   ├── exploit.py                 # 漏洞利用模块
│   ├── persistence.py             # 权限维持模块
│   └── report.py                  # 报告生成模块
├── gpt_helper.py                   # ChatGPT 接口调用封装
└── logs/
    └── scan_log.txt               # 过程日志


安装 Python 和依赖库：
pip install -r requirements.txt

在命令行运行项目主程序：
python main.py --target http://example.com
或者
python main.py --ip 192.168.1.100 --full

阶段            作用
信息收集	      解析端口/子域/Nmap结果，总结服务与风险
漏洞探测	      分析 Nuclei/Nmap/sqlmap 结果，辅助判断 CVE 和风险等级
漏洞利用	      自动生成攻击脚本、构造 payload（Python/Curl 形式）
权限维持	      提议反弹 shell、计划后门策略（如：Netcat 命令生成）
报告生成	      使用 python-docx 自动生成完整 Word 报告






















