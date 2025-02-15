import 'package:car_rec_chatbot/services/auth/auth_gate.dart';
import 'package:car_rec_chatbot/firebase_options.dart';
import 'package:car_rec_chatbot/pages/register_page.dart';
import 'package:car_rec_chatbot/themes/light_mode.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'services/auth/login_or_register.dart';
import 'pages/login_page.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: const AuthGate(),
      theme: darkMode,
    );
  }
}
