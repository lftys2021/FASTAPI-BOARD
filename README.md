# FastAPI Board

FastAPI와 SQLAlchemy를 활용하여 개발한 게시판 API 프로젝트입니다.

## 기술 스택

* Python 3.12
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* JWT Authentication
* Passlib (비밀번호 해시화)

---

# 주요 기능

## 회원 관리

### 회원가입

* 사용자 회원가입
* 비밀번호 해시 저장
* 중복 사용자 검증

### 로그인

* OAuth2 Password Flow 적용
* JWT Access Token 발급

### 내 정보 조회

* 로그인 사용자 정보 조회
* JWT 토큰 인증 적용

### 회원 수정

* 사용자 정보 수정
* 비밀번호 변경 시 재해싱

### 회원 삭제

* 사용자 계정 삭제

---

## 인증 및 권한 관리

### JWT 인증

* Access Token 생성
* Authorization: Bearer <token> 방식 지원

### 인증 사용자 조회

* get_current_user 의존성 사용
* 토큰 검증 후 사용자 조회

### 접근 제어

* 로그인 사용자만 게시글 작성 가능
* 로그인 사용자만 댓글 작성 가능

---

# 게시글 기능

## 게시글 CRUD

### 게시글 생성

* 로그인 사용자만 작성 가능
* 작성자(owner_id) 자동 저장

### 게시글 목록 조회

* 게시글 목록 조회
* 작성자 정보 포함
* 좋아요 수 포함

### 게시글 상세 조회

* 게시글 내용 조회
* 조회수 증가
* 작성자 정보 포함
* 댓글 목록 포함
* 좋아요 수 포함

### 게시글 수정

* 작성자만 수정 가능

### 게시글 삭제

* 작성자만 삭제 가능

---

# 댓글 기능

## 댓글 CRUD

### 댓글 작성

* 로그인 사용자만 작성 가능
* 게시글에 댓글 등록

### 댓글 목록 조회

* 게시글별 댓글 조회

### 댓글 수정

* 작성자만 수정 가능

### 댓글 삭제

* 작성자만 삭제 가능

### 댓글 작성자 표시

* 댓글 작성자(username) 포함

---

# 좋아요 기능

## 게시글 좋아요

### 좋아요 등록

* 로그인 사용자만 가능

### 중복 좋아요 방지

* 동일 사용자의 중복 좋아요 차단

### 좋아요 취소

* 좋아요 삭제 가능

### 좋아요 수 집계

* 게시글 목록 조회
* 게시글 상세 조회

---

## 댓글 좋아요

### 좋아요 등록

* 로그인 사용자만 가능

### 중복 좋아요 방지

* 동일 사용자의 중복 좋아요 차단

### 좋아요 취소

* 좋아요 삭제 가능

### 좋아요 수 집계

* 댓글 조회 시 좋아요 수 표시

---

# 데이터 모델

## User

| 필드              | 설명       |
| --------------- | -------- |
| id              | 사용자 ID   |
| username        | 로그인 ID   |
| email           | 이메일      |
| hashed_password | 암호화 비밀번호 |
| created_at      | 생성일      |
| updated_at      | 수정일      |

---

## Post

| 필드         | 설명     |
| ---------- | ------ |
| id         | 게시글 ID |
| title      | 제목     |
| content    | 내용     |
| owner_id   | 작성자 ID |
| views      | 조회수    |
| created_at | 생성일    |
| updated_at | 수정일    |

---

## Comment

| 필드         | 설명     |
| ---------- | ------ |
| id         | 댓글 ID  |
| content    | 댓글 내용  |
| post_id    | 게시글 ID |
| owner_id   | 작성자 ID |
| created_at | 생성일    |
| updated_at | 수정일    |

---

## Like

게시글 좋아요 정보 저장

| 필드      | 설명     |
| ------- | ------ |
| id      | 좋아요 ID |
| user_id | 사용자 ID |
| post_id | 게시글 ID |

---

## CommentLike

댓글 좋아요 정보 저장

| 필드         | 설명     |
| ---------- | ------ |
| id         | 좋아요 ID |
| user_id    | 사용자 ID |
| comment_id | 댓글 ID  |

---

# API 목록

## 인증

| Method | URL         | 설명      |
| ------ | ----------- | ------- |
| POST   | /signup     | 회원가입    |
| POST   | /login      | 로그인     |
| GET    | /me         | 내 정보 조회 |
| PUT    | /users/{id} | 회원 수정   |
| DELETE | /users/{id} | 회원 삭제   |

---

## 게시글

| Method | URL         |
| ------ | ----------- |
| POST   | /posts      |
| GET    | /posts      |
| GET    | /posts/{id} |
| PUT    | /posts/{id} |
| DELETE | /posts/{id} |

---

## 게시글 좋아요

| Method | URL              |
| ------ | ---------------- |
| POST   | /posts/{id}/like |
| DELETE | /posts/{id}/like |

---

## 댓글

| Method | URL                  |
| ------ | -------------------- |
| POST   | /posts/{id}/comments |
| GET    | /posts/{id}/comments |
| PUT    | /comments/{id}       |
| DELETE | /comments/{id}       |

---

## 댓글 좋아요

| Method | URL                 |
| ------ | ------------------- |
| POST   | /comments/{id}/like |
| DELETE | /comments/{id}/like |

---

# 향후 개발 예정

* 대댓글(Reply)
* 게시글 검색
* 페이징
* 카테고리
* 파일 업로드
* 프로필 이미지
* Refresh Token
* 관리자 권한
* Swagger API 문서 고도화
* Docker 배포
* PostgreSQL 전환
* CI/CD 구축

---

학습 목적의 FastAPI 게시판 프로젝트입니다.
