import sys
import os
import subprocess

from QtFusion.path import abs_path  # 确保abs_path正确设置路径


def run_script(script_path):
    """
      使用当前 Python 环境在项目根目录下运行指定的脚本。

      Args:
          script_path (str): 要运行的脚本的绝对路径

      Returns:
          None
      """
    # 获取当前 Python 解释器的路径
    python_path = sys.executable

    # 确定项目根目录（假设script_path为项目根目录下的web/setup.py）
    project_root = os.path.dirname(os.path.dirname(script_path))

    # 获取脚本相对于项目根目录的路径
    script_relative_path = os.path.relpath(script_path, project_root)

    # 构建运行命令
    command = f'"{python_path}" -m streamlit run "{script_relative_path}"'

    # 在项目根目录下执行命令
    result = subprocess.run(
        command,
        shell=True,
        cwd=project_root  # 关键设置：工作目录设为项目根目录
    )

    if result.returncode != 0:
        print("脚本运行出错，请检查控制台输出。")
    else:
        print("脚本执行成功！")


if __name__ == "__main__":
    # 使用跨平台方式获取脚本绝对路径（示例路径，请根据实际项目结构调整）
    # 假设项目结构为：项目根目录/web/setup.py
    script_path = abs_path("D:\CeShi\webpy-master-web\webpy-master-web\web\setup.py")  # 此处应为实际相对路径

    # 验证路径是否存在
    if not os.path.exists(script_path):
        raise FileNotFoundError(
            f"未找到脚本文件，请检查路径是否正确：{script_path}"
            "\n请确保："
            "\n1. web/setup.py文件存在"
            "\n2. web目录包含__init__.py文件"
            "\n3. 项目结构符合预期"
        )

    # 验证是否包含包初始化文件
    web_dir = os.path.dirname(script_path)
    if not os.path.exists(os.path.join(web_dir, "__init__.py")):
        raise RuntimeError(
            "web目录缺少__init__.py文件，无法作为Python包使用。"
            "\n请创建该文件以支持相对导入。"
        )

    run_script(script_path)
