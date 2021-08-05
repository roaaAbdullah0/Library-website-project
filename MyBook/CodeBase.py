$hostname_localhost ="localhost"; // اتركه كما هو
$database_localhost ="andrody"; // اسم قاعدة البيانات التي قمنا بإنشائها
$username_localhost ="root"; // بين علامات التنصيص ندخل الاسم الخاص للقاعدة او اسم المستخدم للسيرفر الداخلي
$password_localhost =""; // بين علامات التنصيص ندخل كلمة المرور الخاصة بالسيرفر او الخاصة بقاعدة البيانات إذا كنت تستخدمها لموقعك
$localhost = mysql_connect($hostname_localhost,$username_localhost,$password_localhost)
or
trigger_error(mysql_error(),E_USER_ERROR);
 
mysql_select_db($database_localhost, $localhost);
 
$username = $_POST['username'];
$password = $_POST['password'];
$query_search = "select * from users where username = '".$username."' AND password = '".$password. "'";
$query_exec = mysql_query($query_search) or die(mysql_error());
$rows = mysql_num_rows($query_exec);
//echo $rows;
 if($rows == 0) { 
 echo "No Such User Found";  // الرسالة الي تظهر في التطبيق - اسفل زر تسجيل الدخول - في حال إذا لم يتم ايجاد اسم المستخدم في القاعدة
 }
 else  {
	echo "User Found";  // الرسالة التي تظهر اسفل زر تسجيل الدخول في حال تم ايجاد اسم المستخدم .. لا تقم بتعديلها إلا اذا فهمتها, فهي مرتبطة برمجياً مع الكود الخاص بك
}
?>