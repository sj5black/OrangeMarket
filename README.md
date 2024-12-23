# 중고거래 사이트 - 오렌지 마켓🍊
오렌지 마켓은 기본적인 **중고물품 거래** 기능을 제공하는 웹 애플리케이션입니다. 사용자들은 회원가입, 로그인, 물품 등록, 찜하기, 해시태그를 이용한 검색 기능을 제공하며, 인기도순 및 최신순으로 물품을 정렬할 수 있습니다. 또한, 각 유저의 프로필에서 등록한 물품, 찜한 물건, 팔로우 기능 등을 이용할 수 있습니다.

<br><br>

## 목차
<div style="border: 1px solid #333; padding: 10px; background-color: #f9f9f9; width: 250px;">

- [프로젝트 소개](#프로젝트-소개)
- [설치 및 실행](#설치-및-실행)
- [데이터베이스 구조](#데이터베이스-구조)
- [기능별 페이지](#기능별-페이지)
- [ERD](#ERD)
- [트러블슈팅](#트러블슈팅)

</div>

<br><br>

## 프로젝트 소개

- Frontend: HTML, CSS
- Backend: Django, Python
- DB : SQlite3

### 회원 기능

- **회원가입 / 로그인 / 로그아웃**
    - 유저는 username(ID)과 비밀번호로 회원가입 및 로그인을 할 수 있습니다.
    - 로그인 후에는 로그아웃 기능을 제공하여, 언제든지 로그아웃할 수 있습니다.

- **프로필 페이지**
    - 각 유저마다 **프로필 페이지**가 제공됩니다.
    - 프로필 페이지에서는 **유저명**, **가입일**, **내가 등록한 물품 목록**을 확인할 수 있습니다.
    - 유저는 **프로필 사진**을 업로드하여 자신의 사진을 설정할 수 있습니다. 업로드하지 않으면 기본 프로필 사진이 설정됩니다.

    (IMG "기본 프로필 사진 예시")

    - 유저는 **팔로우** 및 **팔로워** 기능을 이용할 수 있으며, 팔로우 및 팔로워 수를 확인할 수 있습니다.

### 유저 기능

- **프로필 페이지**
    - 각 유저의 프로필 페이지에서는 해당 유저가 등록한 물품을 확인할 수 있습니다.
    - 유저는 **팔로우** 버튼을 클릭하여 다른 유저를 팔로우 할 수 있습니다.
    - 팔로워와 팔로우의 수를 확인할 수 있습니다.

### 게시 기능

- **물건 등록, 수정, 삭제**
    - 유저는 물건을 자유롭게 **등록**, **수정**, **삭제**할 수 있습니다.
    - 등록된 물건은 물품 목록과 물품 디테일 페이지에서 볼 수 있습니다.

- **물건 페이지**
    - 물건 페이지에서는 등록된 물품의 제목, 설명, 가격 등을 확인할 수 있습니다.
    - 각 물건에는 **찜하기(Like)** 기능이 있으며, 찜한 수를 확인할 수 있습니다.

- **물건 목록 페이지**
    - 물건 목록에서 물건을 최신순과 인기도순으로 정렬할 수 있습니다.
    - **인기도순**은 찜한 횟수를 기준으로 하며, 동일한 찜수를 가진 물건은 **최신순**으로 정렬됩니다.

    (IMG "물건 목록 정렬 기능 예시")

### 해시태그 기능

- 유저는 각 물건에 **해시태그**를 추가할 수 있습니다.
- 해시태그는 **유일**하며, 중복된 해시태그를 추가할 수 없습니다.
- 해시태그는 띄어쓰기와 특수문자를 허용하지 않으며, 알파벳, 숫자, _만 가능합니다.
- 각 물건에 설정된 해시태그는 물건 목록과 물건 디테일 페이지에서 노출됩니다.

### 검색 기능

- 물건 목록 화면에서 사용자는 **검색어**를 입력하여 물건을 찾을 수 있습니다.
- 검색은 **물건 제목(title)**, **물건 설명(content)**, **회원 유저네임(username)**, **해시태그(hashtag)** 중 하나라도 일치하면 해당하는 물건을 노출합니다.

    (IMG "검색 기능 예시")

<br><br>

## 설치 및 실행

### 요구 사항

- Python 3.x
- Django 4.x
- MySQL 또는 SQLite (기본 DB는 SQLite)

### 설치 방법

1. 리포지토리 클론:

    ```bash
    git clone https://github.com/yourusername/orange-market.git
    ```

2. 가상 환경 설정 (선택 사항):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

3. 종속성 설치:

    ```bash
    pip install -r requirements.txt
    ```

4. 데이터베이스 마이그레이션:

    ```bash
    python manage.py migrate
    ```

5. 서버 실행:

    ```bash
    python manage.py runserver
    ```

6. 브라우저에서 `http://127.0.0.1:8000`에 접속하여 애플리케이션을 사용합니다.

<br><br>

## 🔍 Directory Structure

```
OrangeMarket
│  .gitignore.txt
│  db.sqlite3
│  directory_structure.txt
│  ERD.drawio
│  manage.py
│  README.md
│  references.md
│  requirements.txt
│  
├─accounts
│  │  admin.py
│  │  apps.py
│  │  forms.py
│  │  models.py
│  │  tests.py
│  │  urls.py
│  │  views.py
│  │  __init__.py
│  │  
│  ├─migrations
│  │  │  0001_initial.py
│  │  │  0002_user_followings.py
│  │  │  0003_user_profile_picture.py
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          0001_initial.cpython-312.pyc
│  │          0002_user_followings.cpython-312.pyc
│  │          0003_user_profile_picture.cpython-312.pyc
│  │          __init__.cpython-312.pyc
│  │          
│  ├─templates
│  │  └─accounts
│  │          change_password.html
│  │          login.html
│  │          signup.html
│  │          update.html
│  │          
│  └─__pycache__
│          admin.cpython-312.pyc
│          apps.cpython-312.pyc
│          forms.cpython-312.pyc
│          models.cpython-312.pyc
│          urls.cpython-312.pyc
│          views.cpython-312.pyc
│          __init__.cpython-312.pyc
│          
├─articles
│  │  admin.py
│  │  apps.py
│  │  forms.py
│  │  models.py
│  │  tests.py
│  │  urls.py
│  │  views.py
│  │  __init__.py
│  │  
│  ├─.vs
│  │  │  ProjectSettings.json
│  │  │  slnx.sqlite
│  │  │  VSWorkspaceState.json
│  │  │  
│  │  └─articles
│  │      ├─FileContentIndex
│  │      │      72ec1f9f-199a-4186-863d-bf414f824601.vsidx
│  │      │      
│  │      └─v17
│  ├─migrations
│  │  │  0001_initial.py
│  │  │  0002_article_author.py
│  │  │  0003_comment_author.py
│  │  │  0004_article_like_users.py
│  │  │  0005_article_view_count.py
│  │  │  0006_hashtag_article_hashtags.py
│  │  │  __init__.py
│  │  │  
│  │  └─__pycache__
│  │          0001_initial.cpython-312.pyc
│  │          0002_article_author.cpython-312.pyc
│  │          0002_article_created_at_article_updated_at.cpython-312.pyc
│  │          0003_article_image_alter_article_title.cpython-312.pyc
│  │          0003_comment_author.cpython-312.pyc
│  │          0004_article_like_users.cpython-312.pyc
│  │          0004_comment.cpython-312.pyc
│  │          0005_alter_comment_article.cpython-312.pyc
│  │          0005_article_view_count.cpython-312.pyc
│  │          0006_hashtag_article_hashtags.cpython-312.pyc
│  │          __init__.cpython-312.pyc
│  │          
│  ├─static
│  │  └─articles
│  │          book.png
│  │          orange.png
│  │          placeholder.jpg
│  │          
│  ├─templates
│  │  └─articles
│  │          articles.html
│  │          article_detail.html
│  │          create.html
│  │          update.html
│  │          
│  └─__pycache__
│          admin.cpython-312.pyc
│          apps.cpython-312.pyc
│          forms.cpython-312.pyc
│          models.cpython-312.pyc
│          urls.cpython-312.pyc
│          views.cpython-312.pyc
│          __init__.cpython-312.pyc
│          
├─media
│  ├─images
│  │      product_1.jpg
│  │      product_10.jpg
│  │      product_10_8S4YXXd.jpg
│  │      product_11.png
│  │      product_11_zECk9dc.png
│  │      product_12.png
│  │      product_12_fOSAAY1.png
│  │      product_1_z8BUEEV.jpg
│  │      product_2.jpg
│  │      product_2_U1NZEy4.jpg
│  │      product_3.jpg
│  │      product_3_72aJdIr.jpg
│  │      product_4.jpg
│  │      product_4_JL0MbaB.jpg
│  │      product_5.jpg
│  │      product_5_AeCT93K.jpg
│  │      product_6.jpg
│  │      product_6_R0kr03c.jpg
│  │      product_7.jpg
│  │      product_7_WY9D6Sc.jpg
│  │      product_8.jpg
│  │      product_8_f2IxCDk.jpg
│  │      product_9.jpg
│  │      product_9_QZaDlDm.jpg
│  │      
│  └─profile_pictures
│          assassins_creed_odyssey_002.jpg
│          GitHub.png
│          스크린샷_2023-08-21_225303.png
│          스크린샷_2024-05-27_032616.png
│          스크린샷_2024-05-27_032616_4RPcZqJ.png
│          
├─OrangeMarket
│  │  asgi.py
│  │  settings.py
│  │  urls.py
│  │  wsgi.py
│  │  __init__.py
│  │  
│  └─__pycache__
│          settings.cpython-312.pyc
│          urls.cpython-312.pyc
│          wsgi.cpython-312.pyc
│          __init__.cpython-312.pyc
│          
├─resources
├─static
│  ├─css
│  │      style.css
│  │      
│  └─users
│          user.png
│          
├─templates
│      base.html
│      
└─users
    │  admin.py
    │  apps.py
    │  models.py
    │  tests.py
    │  urls.py
    │  views.py
    │  __init__.py
    │  
    ├─migrations
    │  │  __init__.py
    │  │  
    │  └─__pycache__
    │          __init__.cpython-312.pyc
    │          
    ├─templates
    │  └─users
    │          profile.html
    │          
    └─__pycache__
            admin.cpython-312.pyc
            apps.cpython-312.pyc
            models.cpython-312.pyc
            urls.cpython-312.pyc
            views.cpython-312.pyc
            __init__.cpython-312.pyc
```
---
<br>

## 데이터베이스 구조

- **User**: 유저 정보를 저장하는 테이블
- **Article**: 물건 정보를 저장하는 테이블
- **Hashtag**: 해시태그 정보를 저장하는 테이블
- **Follow**: 팔로우 정보를 저장하는 테이블

<br><br>

## 기능별 페이지

### 물건 목록 페이지

물건 목록 페이지에서 유저는 물건을 최신순 또는 인기도순으로 정렬할 수 있습니다. 각 물건은 찜수와 조회수를 표시하고, 해시태그도 확인할 수 있습니다.

(IMG "물건 목록 페이지 예시")

### 물건 디테일 페이지

물건 디테일 페이지에서는 물건에 대한 자세한 정보와 찜하기 버튼을 확인할 수 있습니다. 물건에 설정된 해시태그도 함께 노출됩니다.

(IMG "물건 디테일 페이지 예시")

### 프로필 페이지

프로필 페이지에서 유저는 자신의 정보를 수정하거나 다른 유저를 팔로우할 수 있습니다. 또한, 자신이 등록한 물품과 찜한 물건을 확인할 수 있습니다.

(IMG "프로필 페이지 예시")

<br><br>

## ERD

(IMG "ERD 이미지")

<br><br>

## 트러블슈팅

1. **게시글을 수정할 때 이미지파일이 수정되지 않는 문제**
    - `enctype="multipart/form-data"`가 `update.html`의 폼에 선언되어있지 않았음
<br>
2. **TemplateSyntaxError at /articles/11/**
    - `Invalid block tag on line 10: 'static', expected 'endif'. Did you forget to register or load this tag?`
    - HTML 파일에 `{% load static %}`이 선언되어 있지 않았음
