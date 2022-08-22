class Product {
  int id;
  String name;
  String description;
  double unitPrice;

  // {} it's name parameter and when you use this, your describe like this name:..., description:..., unitPrice:....
  Product({required this.name, required this.description, required this.unitPrice});
  Product.withId({required this.id, required this.name,required this.description, required this.unitPrice});

  Map<String, dynamic> toMap() {
    var map = Map<String, dynamic>();
    map["name"] = name;
    map["description"] = description;
    map["unitPrice"] = unitPrice;
    if (id != null) {
      map["id"] = id;
    }
    return map;
  }

  Product.fromObject(dynamic o) {
    this.id = o["id"];
    this.name = o["name"];
    this.description = o["description"];
    this.unitPrice = double.tryParse(o["unitPrice"].toString()); //buraya dikkat integer database neden tostring + double parse yapiliyor?
  }
}
 
