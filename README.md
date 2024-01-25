# Service-Backend

이 Repository는 FastAPI를 사용하여 구축된 Image Captioning 및 음성 변환 서비스의 백엔드 부분을 포함하고 있습니다.

## Key Features
- 사용자가 업로드한 이미지에 대한 캡션 생성
- 생성된 캡션을 바탕으로 음성 파일 생성

## Getting Started

### Prerequisites

- Python 3.8 이상

### Installation

1. Clone the repository:
   ```bash
   git clone [Repository URL]
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

- FastAPI 서버 실행:
  ```bash
  uvicorn main:app --reload
  ```

- Docker를 사용한 실행:
  ```bash
  docker build -t service-backend .
  docker run -d --name myservice -p 80:80 service-backend
  ```

## API Reference

- **루트 페이지**: `GET /` - 서비스의 루트 페이지 반환
- **이미지 캡션 생성**: `GET /caption` - 업로드된 이미지에 대한 캡션 반환
- **이미지 업로드 및 처리**: `POST /upload/photo` - 이미지 업로드 후 캡션 및 음성 파일 생성
- **음성 파일 요청**: `POST /wav/{file_name}` - 지정된 파일 이름의 음성 파일 반환

## Folder Structure

- `main.py`: FastAPI 앱의 주 실행 파일
- `photo/`: 업로드된 이미지 저장 폴더
- `template/`: 프론트엔드 템플릿 파일
- `tools/`: OpenAI API 및 기타 도구 모듈

## Docker Support

`Dockerfile`을 사용하여 컨테이너화된 환경에서 서비스를 실행할 수 있습니다.

## License

이 프로젝트는 [MIT 라이선스](LICENSE) 하에 배포됩니다.
