import os

# 定义文件夹路径
safe_folder = "safe"
unsafe_folder = "unsafe"
output_file = "filtered_safe.txt"

# 用于存储 safe 和 unsafe 文件夹中的词语
safe_words = set()
unsafe_words = set()

# 读取 safe 文件夹中的词语
for file_name in os.listdir(safe_folder):
    if file_name.endswith(".txt"):
        with open(os.path.join(safe_folder, file_name), "r", encoding="utf-8") as infile:
            for line in infile:
                # 将词语加入 safe 集合
                safe_words.add(line.strip())

# 读取 unsafe 文件夹中的词语
for file_name in os.listdir(unsafe_folder):
    if file_name.endswith(".txt"):
        with open(os.path.join(unsafe_folder, file_name), "r", encoding="utf-8") as infile:
            for line in infile:
                # 将词语加入 unsafe 集合
                unsafe_words.add(line.strip())

# 从 safe 集合中移除 unsafe 集合的词语
filtered_safe_words = safe_words - unsafe_words

# 将结果写入输出文件
with open(output_file, "w", encoding="utf-8") as outfile:
    for word in sorted(filtered_safe_words):  # 按字母顺序排序
        outfile.write(word + "\n")

print(f"处理完成，过滤后的词语已保存到 {output_file}")
