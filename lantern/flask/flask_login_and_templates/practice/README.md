# to start work on project being in practice folder

    $ pip install -r grocery_store/requirements.txt
    $ pip install -e .
    $ python grocery_store/manage.py db upgrade
    $ python grocery_store/manage.py populate

To run server:

    $ python grocery_store/manage.py runserver

If something incomprehensible happened (^^,) :

    $ git stash list ## look at commit hash in stash/vault
    $ git branch tmp f4ea068 ## use commit to create temporary branch from it
    $ git branch -m hw_flask_all_goods_list ## just rename branch
    $ git push origin hw_flask_all_goods_list