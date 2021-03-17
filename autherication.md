# Domen: http://edu.uzdevelop.ru/

# Autherication

## Three type of people can log in. They are:  

                                1) Teacher
                                2) Student
                                3) Leader

## Request for creating teacher:  

    method: POST
    url: http://127.0.0.1:8000/api/v1/users/teacher/create/
    request:
    ```json
        {
            "username": "Rahimjon_A",
            "first_name": "Rahimjon",
            "last_name": "Abduganiev",
            "email": "abduganievrahimjon@gmail.com",
            "image": "url",
            "bio": "Cool!!!",
            "experience": "2 years",
            "sex": "Male",
            "phone": "998998406046"
        }  

## Request for teachers list:  

    method: GET
    url: http://127.0.0.1:8000/api/v1/users/teacher/list/
    request::
    ```json
        {
            "id": 2,
            "image": null,
            "bio": "Cool!",
            "experience": "2 years",
            "sex": "Male",
            "birthday": "2021-02-09",
            "phone": "998998406046"
        }

## Request for updating teacher:  

    method: PATCH
    url: http://127.0.0.1:8000/api/v1/users/teacher/update/<:id>
    request:
    ```json
        {
            "username": "Rahimjon_B",
            "first_name": "Rahimjon",
            "last_name": "Abduganiev",
            "email": "abduganievrahimjon@gmail.com",
            "image": "url",
            "bio": "Cool!!!",
            "experience": "2 years",
            "sex": "Male",
            "phone": "998998406046"
        }


## Request for creating student:  

    method: POST
    url: http://127.0.0.1:8000/api/v1/users/student/create/
    request:
    ```json
        {
            "username": "Rahimjon_A",
            "first_name": "Rahimjon",
            "last_name": "Abduganiev",
            "email": "abduganievrahimjon@gmail.com",
            "image": "url",
            "sex": "Male",
            "birthday": "2021-02-09",
            "phone": "998998406046"
        }

## Request for students list:  

    method: GET
    url: http://127.0.0.1:8000/api/v1/users/student/list/
    ```json
        {
        "id": 1,
        "image": "http://127.0.0.1:8000/student_poster/siniy.png",
        "sex": "Male",
        "birthday": "2002-07-04",
        "phone": "998991011441"
        }

## Request for updating student:  

    method: PATCH
    url: http://127.0.0.1:8000/api/v1/users/student/update/<:id>
    ```json
        {
            "username": "Rahimjon_B",
            "first_name": "Rahimjon",
            "last_name": "Abduganiev",
            "email": "abduganievrahimjon@gmail.com",
            "image": "url",
            "sex": "Male",
            "birthday": "2021-02-09",
            "phone": "998998406046"
        }


## There is a only one leader, that's why people don't have to see him at web site.