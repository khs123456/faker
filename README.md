# 사기 궁합앱
다 낚을 거야!

## 1. App의 구조
1. `/` : 메인페이지
    - 이름을 입력 받는다.

`
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>짝</title>
</head>
<body>
    <h1>궁합을 봐 드립니다.</h1>
    <form action="/result">
        <label>당신의 이름</label>
        <input type="text" name="name1"><br>
        <label>그분의 이름</label>
        <input type="text" name="name2"><br>
        <input type="submit">
    </form>
</body>
</html>
`

2. `/result` : 결과페이지
    - 가짜 궁합을 보여준다.
    - csv에 입력값을 저장한다.

3. `/admin` : 어드민페이지
    - 저장된 이름들을 csv에서 불러와 출력한다


## 2. (번외)