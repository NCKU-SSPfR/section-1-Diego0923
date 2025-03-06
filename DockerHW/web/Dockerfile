FROM python:3.11-slim

# 設置工作目錄
WORKDIR /app

# 複製應用程式的所有文件到容器內
COPY . .

# 安裝 Python 依賴
RUN pip install --no-cache-dir -r requirements.txt

# 暴露應用程式的 Port
EXPOSE 5000 

CMD ["python", "main.py"]
