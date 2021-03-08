dir=$(date "+%Y%m%d");
mkdir -m 777 -p /tmp/$dir
date
for db in convinceme fourforums createdebate createdebate_released; do
     echo $db;
     mkdir -m 777 /tmp/$dir/$db;
     mysqldump --tab=/tmp/$dir/$db $db;
     rm /tmp/$dir/$db/*.sql;
     mysqldump --no-data $db -r /tmp/$dir/$db/$db.sql;
     echo "compressing";
     tar -czf /tmp/$dir/"$db"_$(date +%Y_%m_%d).tgz -C /tmp/$dir/ $db;
     rm -rf /tmp/$dir/$db;
done; mv /tmp/$dir .; date;

cd $dir
date
for db in convinceme fourforums createdebate createdebate_released; do
    echo $db;
    mysql -u root -p -e "CREATE SCHEMA $db DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_bin; SET GLOBAL foreign_key_checks=0";
    mysql -u root -p $db < $db/$db.sql;
    mysqlimport -u root -p --local $db $db/*.txt;
    mysql -u root -p -e "SET GLOBAL foreign_key_checks=1";
done;date;