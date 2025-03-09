# TODO: Install the backend dependency package into the app folder inside the container.

# 使用 Python 3.11 官方映像作為基礎映像
FROM python:3.11

# 設定容器內的工作目錄為 /app
WORKDIR /app

# 複製本機的 requirements.txt 依賴檔案到容器內的 /app/requirements.txt
COPY ./requirements.txt /app/requirements.txt

# 安裝 Python 依賴套件
RUN pip install -r /app/requirements.txt

# 創建一個名為 myuser 的非 root 使用者，並指定 UID 為 1000
RUN useradd -m -u 1000 myuser

# 將 /app 目錄的擁有者變更為 myuser
RUN chown -R myuser:myuser /app

# 複製本機的 src 目錄到容器內的 /app/src，並設定擁有者為 myuser
COPY --chown=myuser:myuser ./src/ /app/src

# 切換為非 root 使用者 myuser，後續所有指令都會以這個使用者執行
USER myuser

# 執行 FastAPI 應用，使用 Uvicorn 作為 ASGI 伺服器
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

