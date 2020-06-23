# Шпаргалка 

## В цьому репозиторії ви зможете знайти матеріал лекцій та домашні 

## Як створити fork

Офіційна документація, як створити fork  
https://help.github.com/en/github/getting-started-with-github/fork-a-repo

Ссилка на основний репозиторій в якому буде код з лекцій та практики
https://github.com/Vasilov345/green_lantern

## Як зв'язати свій fork з основним репозиторієм і отримувати з нього зміни

Перейдіть в директорію свого проекту
```
git remote -v 
```
На виході буде ссилка на ваш репозиторій
```
origin https://github.com/{github_nickname}/green_lantern.git (fetch)  
origin https://github.com/{github_nickname}/green_lantern.git (push)  
```

```
git remote add upstream https://github.com/Vasilov345/green_lantern.git
git remote -v
```
На виході буде дві ссилки на ваш fork(origin), та основний репозиторій (upstream)

```
origin	https://github.com/{github_nickname}/green_lantern.git (fetch)
origin	https://github.com/{github_nickname}/green_lantern.git (push)
upstream  https://github.com/Vasilov345/green_lantern.git (fetch)
upstream  https://github.com/Vasilov345/green_lantern.git (push)
```

## Практика

На початку заняття викладач надає студентам назву гілки, з якою буде проходити робота протягом заняття

Студент, який кодить разом з викладачем стягує цю гілку з основного репозиторію та створює власну в своєму форку
```
git fetch upstream
git checkout upstream/practice_branch
git chechout -b student_practice_branch
```

Коли код написаний в достатній степені, щоб разшарити його іншим студентам, то  код комітиться в бранчу студента.  
Потім студент створює PR з свого форку в основний репозиторій.  
origin/student_practice_branch -> upstream/practice_branch
```
git add {changes_for_commit}
git commit -m "Some important changes or other msg to specify changes enough widely "
git push origin student_practice_branch

```

Далі викладач приймає або відхиляє PR і код написаний студентом зявляється в основному репозиторії

## Приємного навчання :)
