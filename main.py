import pytest

if __name__ == '__main__':
    # pytest.main()  # 执行pytest命令，去收集用例，然后执行用例。当前文件所在的目录为rootdir
    pytest.main(["--alluredir=report"])
    print("test")