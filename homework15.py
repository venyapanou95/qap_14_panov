# Linux
# Создайте 3 директории:
# cl_work
# delete_me_please
# copy_dir
# Задание 1:
cd delete_me_please
touch aivazovsky_biography.txt
echo 'Иван Константинович Айвазовский. Боиграфия: https://en.wikipedia.org/wiki/Ivan_Aivazovsky' >> aivazovsky_biography.txt
cat aivazovsky_biography.txt
mv aivazovsky_biography.txt ../cl_work/

# Задание 2:

# 1. Перейдите в директорию copy_dir
cd ../copy_dir

# 2. Создайте директорию <Ваше_имя>
mkdir <aqapy>

# 3. В созданной директории создайте файл i_love_linux.txt
touch i_love_linux.txt

# 4. Скопируйте директорию <Ваше_имя> в cl_work
cd ../../cl_work

# Убедитесь, что в директории cl_work находится aivazovsky_biography.txt и директория с Вашим именем
cp -r ../copy_dir/<aqapy> .
