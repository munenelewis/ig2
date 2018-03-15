{% include 'base.html' %} {% block content %}
<!--
<style>
    @media(max-width: 640px) and (min-width:360px) {
        .h1,
        h1 {
            font-size: 75px;
        }
        body {
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            font-size: 14px;
            line-height: 1.42857143;
            color: #333;
            background-color: #d81212;
        }
    }
</style>

<div class="container">
    <div class="row">

        <div class="col-md-8">






        </div>
        <div class="col-md-4">
            <h2>Other people</h2>



            <h2>Friends</h2>

            {% for friend in friends %}
            <a href="#">
                <h3>{{ friend.users.firstname }}</h3>
            </a>
            <a href="#">
                <button type="button" class="btn btn-default">Unfollow</button>
            </a>
            {% endfor %}
        </div>


    </div>

</div>


-->


<style type="text/css">
    body {
        background-color: #fafafa;
        padding: 60px;
        font-family: 'Droid Sans', sans-serif;

    }

    a {
        text-decoration: none;
    }

    .Instagram-card {
        background: #ffffff;
        border: 1px solid #f2f2f2;
        border-radius: 3px;
        width: 100%;
        max-width: 600px;
        margin: auto;

    }

    .Instagram-card-header {
        padding: 20px;
        height: 40px;
    }

    .Instagram-card-user-image {
        border-radius: 50%;
        width: 40px;
        height: 40px;
        vertical-align: middle;
    }

    .Instagram-card-time {
        float: right;
        width: 80px;
        padding-top: 10px;
        text-align: right;
        color: #999;
    }

    .Instagram-card-user-name {
        margin-left: 20px;
        font-weight: bold;
        color: #262626;
    }

    .Instagram-card-content {
        padding: 20px;
    }

    .Likes {
        font-weight: bold;
    }

    .Instagram-card-content-user {
        font-weight: bold;
        color: #262626;
    }

    .hashtag {
        color: #003569;
    }

    .comments {
        color: #999;
    }

    .user-comment {
        color: #003569;
    }

    .Instagram-card-footer {
        padding: 20px;
        display: flex;
        align-items: center;
    }

    hr {
        border: none;
        border-bottom: 1px solid #ccc;
        margin-top: 30px;
        margin-bottom: 0px;
        padding-bottom: 0px;

    }


    .footer-action-icons {
        font-size: 16px;
        color: #ccc;
    }

    .comments-input {
        border: none;
        margin-left: 10px;
        width: 100%;
    }

    .Instagram-card-user-image {
        border-radius: 50%;
        width: 71px;
        height: 59px;
        vertical-align: middle;
    }

    .scroll {
        background-color: #eee;
        width: 274px;
        height: 307px;
        border: 1px dotted black;
        overflow-x: hidden;
        overflow-y: scroll;
    }


    @media (max-width: 640px) and (min-width: 360px) {
        .scroll {
            background-color: #eee;
            width: 571px;
            height: 96px;
            border: 1px dotted black;
            overflow-x: scroll;
            /* overflow-y: scroll; */
            /* float: right; */
            margin-top: -1307px;
            position: fixed;
            /* margin-left: 1009px; */
        }
    }

    .form-control {
        display: block;
        width: 241%;
        height: 34px;
        padding: 6px 12px;
        font-size: 14px;
        line-height: 1.42857143;
        color: #555;
        background-color: #fff;
        background-image: none;
        border: 1px solid #ccc;
        border-radius: 4px;
        -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075);
        box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075);
        -webkit-transition: border-color ease-in-out .15s, -webkit-box-shadow ease-in-out .15s;
        -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
        transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
    }
</style>
</head>

<body>
    <div class="row">
        <div class="class-md-12">

            <div class="col-md-8">

                <div class="Instagram-card">
                    <div class="Instagram-card-header">
                        <img src="https://scontent.fnbo1-1.fna.fbcdn.net/v/t1.0-9/26169922_1237830159695333_3267117830949697715_n.jpg?_nc_eui2=v1%3AAeHLKPWlKUDdF7KY7n1LyQUIvu80GWv-Qn2cWe7C7lQiyJfwg1Ju-l2NdLAy9KYn009ymUv4CazstNrFsJmVAyF0hil1lhtogszoVS20HqigMg&oh=da71aa212302a908be25de45f7963fb2&oe=5B4BDD29"
                            class="Instagram-card-user-image">
                        <a class="Instagram-card-user-name" href="https://www.instagram.com/rogersbase/"> irimiah lewis </a>
                        <div class="Instagram-card-time"> 23h ago </div>
                    </div>

                    <div class="Instagram-card-image">
                        <img src="http://globalmedicalco.com/photos/globalmedicalco/13/64057.jpg" height="600px/" style="width: 600px;"> </div>

                    <div class="Instagram-card-content">
                        <p class="Likes">640 Me gusta</p>
                        <p>
                            <a class="Instagram-card-content-user">
                                    <a class="footer-action-icons" href="#">
                                            <i class="fa fa-heart-o"></i>
                                        </a>
                                    <br> {% for post in posts %}
                                <href="https://www.instagram.com/rogersbase/">rogersbase</a>
                            I GOT TO PLAY NINTENDO SWITCH ON #NINTENDO MINUTE! 😱 So happy that I can finally talk about this! @kitellis and @breath0air
                            told me that we were going to be playing

                            

                            <a class="user-comment" href="#"><b style="margin-right: 12px;">{{ post.user}}</b></a>{{post.post}}
                            <br/> <i style="float:  right;">{{post.created}}</i>
                        </p>




                        {% endfor %}


                        <hr>
                    </div>

                    <div class="Instagram-card-footer">
                        <form method="post">
                            {% csrf_token %} {{form.errors}} {{form.post}}

                            <button type="submit">submit</button>

                        </form>
                      

                        <a class="footer-action-icons" href="#">
                            <i class="fa fa-ellipsis-h"></i>
                        </a>
                    </div>



                </div>

            </div>

            <div class="col-md-4" sty>
                <div class="scroll"> {% for user in users %}

                    <a href="{{ 'profile' }}">
                        <h4> {{user.username}}</h4>
                    </a>

                    {% endfor %}</div>
            </div>

        </div>

    </div>



    {% endblock %}