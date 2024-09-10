import requests
from bs4 import BeautifulSoup

# 示例PDB ID列表
pdb_ids = ["1C0A", "2D2F", "6C09"]  # 在这里替换成你的PDB ID列表

for pdb_id in pdb_ids:
    # 构建请求URL
    url = f"https://www.rcsb.org/structure/{pdb_id}"

    try:
        # 发送GET请求获取网页内容，设置verify=False来忽略SSL验证
        response = requests.get(url, verify=False)

        # 检查请求是否成功
        if response.status_code == 200:
            # 使用BeautifulSoup解析HTML
            soup = BeautifulSoup(response.content, 'html.parser')

            # 查找表达体系信息
            expression_system = soup.find('li', id='header_expression-system')

            if expression_system:
                # 提取表达体系文本
                expression_system_text = expression_system.get_text(strip=True).replace('Expression System:',
                                                                                        '').strip()
                print(f"PDB ID: {pdb_id}, Expression System: {expression_system_text}")
            else:
                print(f"PDB ID: {pdb_id}, Expression System: Not Found")
        else:
            print(f"Failed to fetch data for PDB ID: {pdb_id}, Status Code: {response.status_code}")
    except requests.exceptions.SSLError as e:
        print(f"SSL Error for PDB ID: {pdb_id}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request Error for PDB ID: {pdb_id}: {e}")
