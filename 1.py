from PIL import Image
import numpy as np
import imageio

# 图片路径
image_path = './files/icon.jpg'
# 输出视频路径
video_path = './videos/32.mp4'

# 打开图片
image = Image.open(image_path)

# 将图片转换为所需的模式，例如"RGB"
if image.mode != 'RGB':
    image = image.convert('RGB')

# 定义帧率
fps = 24

# 创建一个Writer对象，用于写入视频
writer = imageio.get_writer(video_path, fps=fps)

# 假设我们想创建10秒的视频
for i in range(fps * 10):
    # 将图片写入视频
    writer.append_data(np.array(image))

# 完成视频写入
writer.close()

print(f"Video has been created: {video_path}")