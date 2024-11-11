# Python 3.11 이미지 사용
FROM python:3.11

# 작업 디렉토리 설정
WORKDIR /djangoapps

# requirements.txt 복사 및 패키지 설치
COPY requirements.txt .
RUN pip install -r requirements.txt

# MySQL 클라이언트 설치 추가
RUN apt-get update && apt-get install -y default-mysql-client && apt-get clean

# wait-for-it.sh 스크립트를 복사하고 실행 권한 부여
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# 애플리케이션 파일 복사
COPY . .

# 컨테이너에서 노출할 포트 설정
EXPOSE 8000

# MySQL 서버가 준비될 때까지 대기 후 Django 서버 실행
CMD ["/wait-for-it.sh", "docker-mysql:3306", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
