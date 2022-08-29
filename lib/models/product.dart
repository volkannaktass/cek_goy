class Product {
  int id;
  String name;
  String description;
  double unitPrice;
  //int user_id;

  // {} it's name parameter and when you use this, your describe like this name:..., description:..., unitPrice:....
  Product({required this.name, required this.description, required this.unitPrice});
  Product.withId({required this.id, required this.name,required this.description, required this.unitPrice});

  Map<String, dynamic> toMap() {
    var map = Map<String, dynamic>();
    map["name"] = name;
    map["description"] = description;
    map["unitPrice"] = unitPrice;
    //map["user_id"] = user_id;
    if (id != null) {
      map["id"] = id;
    }
    return map;
  }

  Product.fromObject(dynamic o) {
    this.id = o["id"]!;
    this.name = o["name"]!;
    this.description = o["description"]!;
    this.unitPrice = double.tryParse(o["unitPrice"].toString())!; //buraya dikkat integer database neden tostring + double parse yapiliyor?
    //this.user_id = o["user_id"];
  }
}
 
