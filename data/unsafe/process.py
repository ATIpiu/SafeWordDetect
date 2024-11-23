import os

# 定义汇总文件名称
output_file = "unsafe.txt"

# 使用集合去重
unique_lines = set()

# 遍历当前目录下的所有文件
for file_name in os.listdir("."):
    # 检查文件是否以 .txt 结尾且不是目标输出文件
    if file_name.endswith(".txt") and file_name != output_file:
        with open(file_name, "r", encoding="utf-8") as infile:
            for line in infile:
                # 去掉行尾的换行符后添加到集合
                unique_lines.add(line.strip())

# 将去重后的内容写入新的文件
with open(output_file, "w", encoding="utf-8") as outfile:
    for line in sorted(unique_lines):  # 按字母顺序排序写入
        outfile.write(line + "\n")

print(f"汇总并去重完成，结果已保存到 {output_file}")