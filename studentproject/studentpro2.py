db={1:['mohit','bca',['java','python','php']],
    2:['jay','bcs',['c','python','sql']],
    3:['vijay','bsc',['c++','sql','php']],
    4:['kiran','bcs',['java','python','php']],
    5:['viru','bsc',['android','java','php']],
    6:['ankit','bca',['java','python','sql']],
    7:['nikhil','bca',['java','android','c++']]}
def menu():
    print("_"*130)
    print()
    print('\t\t\t\t\t WELCOME TO THE STUDENT MANAGEMENT SYSTEM')
    print("_"*130)
    print('''
                                 \t\t\tOperations


                            \t\t\t1---> create student data
                            \t\t\t2---> display student data
                            \t\t\t3---> delete student data
                            \t\t\t4---> search student by s_class
                            \t\t\t5---> update student data
                            \t\t\t6---> search student by sub

         ''')
    print("_"*130)
    print()
menu()

def create():
    
    
    if len(db)>0:
        s_id=int(input('enter id of the student : '))
        if s_id not in db:
            s_name=input('enter name of the student : ')
            s_class=input('enter class of the student : ').lower()
            sub1=input('enter first sub of the student : ').lower()
            sub2=input('enter second sub of the student : ').lower()
            sub3=input('enter third sub of the student : ').lower()
            li=[]
            li.append(s_name)
            li.append(s_class)
            subl=[]
            subl.append(sub1)
            subl.append(sub2)
            subl.append(sub3)
            print(sub1)

            li.append(subl)
          

            db[s_id]=li
            print(f'{s_name} Data created successfully into database ')
        else:
            print(f'{s_id} is already present in the database ')

    else:
        print('Empty Database')

def display():
    
    if len(db)>0:
        print('_'*106)
        print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Roll no','s_name','s_class','sub1','sub2','sub3'))
        print('_'*106)
        for i in db:
            print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(i,db[i][0],db[i][1],db[i][2][0],db[i][2][1],db[i][2][2]))
        print('_'*106)
        print()     
    else:
        print('empty database')

def delete():
    if len(db)>0:
        s_id=int(input('enter id of the student whose data you want to delete: '))
        if s_id  in db:
            del db[s_id]
            

            print(f'{s_id} Data deleted successfully from database ')
        else:
            print(f'{s_id} is not present in the database ')

    else:
        print('Empty Database')

def search():
    if len(db)>0:
        print("_"*130)
        print('''  
                      \t\t subject search Operations
                     \t\t\t ________________________

                \t\t\t 1----python
                \t\t\t 2----java
                \t\t\t 3----sql
                \t\t\t 4----android
                \t\t\t 5----c
                \t\t\t 6----c++
                \t\t\t 7----php
                           
        ''')
        print("_"*130)
        print()
        subj=int(input('enter sub index : '))
        if subj==1:
            print('_'*106)
            print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Roll no','s_name','s_class','sub1','sub2','sub3'))
            print('_'*106)
            for i in db:
                if 'python' in db[i][2]:
                    print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(i,db[i][0],db[i][1],db[i][2][0],db[i][2][1],db[i][2][2]))
            print('_'*106)
            print()
        elif subj==2:
            print('_'*106)
            print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Roll no','s_name','s_class','sub1','sub2','sub3'))
            print('_'*106)
            for i in db:
                if 'java' in db[i][2]:
                    print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(i,db[i][0],db[i][1],db[i][2][0],db[i][2][1],db[i][2][2]))
            print('_'*106)
            print()

        elif subj==3:
            print('_'*106)
            print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Roll no','s_name','s_class','sub1','sub2','sub3'))
            print('_'*106)
            for i in db:
                if 'sql' in db[i][2]:
                    print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(i,db[i][0],db[i][1],db[i][2][0],db[i][2][1],db[i][2][2]))
            print('_'*106)
            print()

        elif subj==4:
            print('_'*106)
            print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Roll no','s_name','s_class','sub1','sub2','sub3'))
            print('_'*106)
            for i in db:
                if 'android' in db[i][2]:
                    print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(i,db[i][0],db[i][1],db[i][2][0],db[i][2][1],db[i][2][2]))
            print('_'*106)
            print()

        elif subj==5:
            print('_'*106)
            print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Roll no','s_name','s_class','sub1','sub2','sub3'))
            print('_'*106)
            for i in db:
                if 'c' in db[i][2]:
                    print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(i,db[i][0],db[i][1],db[i][2][0],db[i][2][1],db[i][2][2]))
            print('_'*106)
            print()

        elif subj==6:
            print('_'*106)
            print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Roll no','s_name','s_class','sub1','sub2','sub3'))
            print('_'*106)
            for i in db:
                if 'c++' in db[i][2]:
                    print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(i,db[i][0],db[i][1],db[i][2][0],db[i][2][1],db[i][2][2]))
            print('_'*106)
            print()

        elif subj==7:
            print('_'*106)
            print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Roll no','s_name','s_class','sub1','sub2','sub3'))
            print('_'*106)
            for i in db:
                if 'php' in db[i][2]:
                    print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(i,db[i][0],db[i][1],db[i][2][0],db[i][2][1],db[i][2][2]))
            print('_'*106)
            print()
        else:
            print('Invalid operation taken')

    else:
        print('Empty Database')

def update():
        print("_"*130)
        print('''  
                      \t\t Update Operations
                     \t\t\t _______________

                \t\t\t 1----Name
                \t\t\t 2----s_class
                \t\t\t 3----subject
                           
        ''')
        print("_"*130)
        print()

        ch=int(input('enter Update Operation '))
        if ch==1:
            s_id=int(input('enter id of the student whose name you want to update : '))
            if s_id in db:
                s_name=input('enter new name of the student : ')
                db[s_id][0]=s_name
                print(f'Name updated successfully ')
            else:
                print(f'{s_id} is not present in the database')
        
        if ch==2:
            s_id=int(input('enter id of the student whose class you want to update : '))
            if s_id in db:
                s_class=input('enter new class of the student : ')
                db[s_id][1]=s_class
                print(f'class updated successfully ')
            else:
                print(f'{s_id} is not present in the database')

        if ch==3:
            print("_"*130)
            print('''  
                      \t\t subject Update Operations
                     \t\t\t ________________________

                \t\t\t 1----sub1
                \t\t\t 2----sub2
                \t\t\t 3----sub3
                           
            ''')
            print("_"*130)
            print()
            id=int(input('enter id of the student whose sub you want to update : '))
            sch=int(input('enter subject Update Operation '))
            if sch==1:
                sub1=input('enter new first sub : ')
                db[id][2][0]=sub1
                print('sub1 updated successfully ')
            elif sch==2:
                sub2=input('enter new second sub : ')
                db[id][2][1]=sub2
                print('sub2 updated successfully ')
            elif sch==3:
                sub3=input('enter new third sub : ')
                db[id][2][2]=sub3
                print('sub3 updated successfully ')
            else:
                print('please enter valid choice ')
    
def classsearch():
    if len(db)>0:
        print("_"*130)
        print('''  
                      \t\t s_class search Operations
                     \t\t\t ________________________

                \t\t\t 1----bca
                \t\t\t 2----bcs
                \t\t\t 3----bsc
               
                           
        ''')
        print("_"*130)
        print()
        sclass=int(input('enter sub index : '))
        if sclass==1:
            print('_'*106)
            print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Roll no','s_name','s_class','sub1','sub2','sub3'))
            print('_'*106)
            for i in db:
                if 'bca' in db[i][1]:
                    print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(i,db[i][0],db[i][1],db[i][2][0],db[i][2][1],db[i][2][2]))
                    print('_'*106)
            print()
        elif sclass==2:
            print('_'*106)
            print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Roll no','s_name','s_class','sub1','sub2','sub3'))
            print('_'*106)
            for i in db:
                if 'bcs' in db[i][1]:
                    print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(i,db[i][0],db[i][1],db[i][2][0],db[i][2][1],db[i][2][2]))
                    print('_'*106)
            print()

        elif sclass==3:
            print('_'*106)
            print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Roll no','s_name','s_class','sub1','sub2','sub3'))
            print('_'*106)
            for i in db:
                if 'bsc' in db[i][1]:
                    print('|{:^15}|{:^25}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(i,db[i][0],db[i][1],db[i][2][0],db[i][2][1],db[i][2][2]))
                    print('_'*106)
            print()

while True:
    op=int(input('Enter operation you want : '))
    print()
    if op==1:
        create()
    elif op==2:
        display()
    elif op==3:
        delete()
    elif op==4:
        search()
    elif op==5:
        update()
    elif op==6:
        classsearch()
    else:
        print('please enter valid operation  ')
    ch=input("Do you want to continue [y/n]: ")
    if ch.lower()!='y':
        print("THANK YOU ")
    