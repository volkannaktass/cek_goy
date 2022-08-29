class User{
  int id;
  String userName;
  String firstName;
  String lastName;
  int password;
  String email;
  int phoneNumber;
  double rate;


  User({required this.userName,required this.firstName,required this.lastName,required this.password,required this.email,required this.phoneNumber,required this.rate});
  User.withId({required this.id,required this.userName,required this.firstName,required this.lastName,required this.password,required this.email,required this.phoneNumber,required this.rate});

  Map<String, dynamic> toMap() {
    var map = Map<String, dynamic>();
    map["userName"] = userName;
    map["firstName"] = firstName;
    map["lastName"] = lastName;
    map["password"] = password;
    map["email"] = email;
    map["phoneNumber"] = phoneNumber;
    map["rate"] = rate;
    if (id != null) {
      map["id"] = id;
    }
    return map;
  }


  User.fromObject(dynamic o) {
    this.id = o["id"];
    this.userName = o["userName"];
    this.firstName = o["firstName"];
    this.lastName = o["lastName"];
    this.password = o["password"];
    this.email = o["email"];
    this.phoneNumber = o["phoneNumber"];
    this.rate = double.tryParse(o["rate"].toString())!;
      
  }


}
