import os

# 汇总文件的名称
output_file = "汇总结果.txt"

# 打开汇总文件以写入模式
with open(output_file, "w", encoding="utf-8") as outfile:
    # 遍历当前目录下的所有文件
    for file_name in os.listdir("."):
        # 检查文件是否以 .txt 结尾且不是汇总文件本身
        if file_name.endswith(".txt") and file_name != output_file:
            with open(file_name, "r", encoding="utf-8") as infile:
                for line in infile:
                    # 提取行中的第一个字段（以制表符为分隔）
                    first_field = line.split("\t")[0]
                    outfile.write(first_field + "\n")

print(f"汇总完成，结果已保存到 {output_file}")
