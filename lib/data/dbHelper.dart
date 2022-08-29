import 'dart:async';
import 'package:cek_goy/models/product.dart';
import 'package:cek_goy/models/user.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
class DbHelper{

late final Database _db;

  Future<Database> get db async {
    if (_db == null) {
      _db = await initializeDb();
    }
    return _db;
  }

  Future<Database> initializeDb() async {
    String dbPath = join(await getDatabasesPath(), "etrade.db");
    var eTradeDb = await openDatabase(dbPath, version: 1, onCreate: createDb);
    return eTradeDb;
  }


  void createDb(Database db, int version) async {
    await db.execute("Create table users(id integer primary key, userName text, firstName text, lastName text, password integer, email text, phoneNumber integer, rate integer)");
    await db.execute("Create table products(id integer primary key, user_id INTEGER NOT NULL, name text, description text, unitPrice integer,FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE NO ACTION ON UPDATE NO ACTION)");
  }

  Future<List<Product>> getProducts() async { 
    Database db = await this.db;
    var result = await db.query("products");
    return List.generate(result.length, (i){
        return Product.fromObject(result[i]);
    });
  }

  Future<List<User>> getUsers() async {
    Database db = await this.db;
    var result = await db.query("users");
    return List.generate(result.length, (i){
      return User.fromObject(result[i]);
    });
  }



  Future<int> insertProduct(Product product) async {
    Database db = await this.db;

    var result = await db.insert("products",product.toMap());
    return result;
  }


  Future<int> insertUser(User user) async {
    Database db = await this.db;

    var result = await db.insert("users",user.toMap());
    return result;
  }


    
  Future<int> deleteProduct(int id) async {
    Database db = await this.db;

    var result = await db.rawDelete("delete from products where id= $id");
    return result;
    
  }


  Future<int> deleteUser(int id) async {
    Database db = await this.db;

    var result = await db.rawDelete("delete from users where id= $id");
    return result;

  }


  Future<int> updateProduct(Product product) async {
    Database db = await this.db;

    var result = await db.update("products", product.toMap(), where: "id=?", whereArgs: [product.id]);
    return result;
    
  }


  Future<int> updateUser(User user) async {
    Database db = await this.db;

    var result = await db.update("users", user.toMap(), where: "id=?", whereArgs: [user.id]);
    return result;

  }
  
}
