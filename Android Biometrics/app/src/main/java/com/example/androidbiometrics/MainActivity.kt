package com.example.androidbiometrics

import android.annotation.SuppressLint
import android.app.Dialog
import android.app.KeyguardManager
import android.content.Context
import android.content.DialogInterface
import android.content.Intent
import android.content.pm.PackageManager
import android.hardware.biometrics.BiometricManager
import android.hardware.biometrics.BiometricPrompt
import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.CancellationSignal
import android.view.View
import android.widget.Button
import android.widget.Toast
import androidx.annotation.RequiresApi
import androidx.core.app.ActivityCompat

class MainActivity : AppCompatActivity() {

    private var cancelSignal: CancellationSignal? = null
    private val authenticationCallback: BiometricPrompt.AuthenticationCallback
    get() =
        @RequiresApi(Build.VERSION_CODES.P)
        object : BiometricPrompt.AuthenticationCallback() {
            override fun onAuthenticationError(errorCode: Int, errString: CharSequence?) {
                super.onAuthenticationError(errorCode, errString)
                notificationPopup("Authentication Error: $errString")
            }

            override fun onAuthenticationSucceeded(result: BiometricPrompt.AuthenticationResult?) {
                super.onAuthenticationSucceeded(result)
                notificationPopup("Authentication Successful!")
                startActivity(Intent(this@MainActivity, SecondaryActivity::class.java))
            }
        }

    @RequiresApi(Build.VERSION_CODES.P)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        checkCompatability()

        val button = findViewById<View>(R.id.auth_button)
        button.setOnClickListener {
            val biometricPrompt = BiometricPrompt.Builder(this)
                .setTitle("Please authenticate with a registered fingerprint.")
                .setSubtitle("Authentication is required.")
                .setDescription("This application uses fingerprint authentication.")
                .setNegativeButton("Cancel", this.mainExecutor, DialogInterface.OnClickListener {dialog, which -> notificationPopup("Authentication has been cancelled.")}).build()

            biometricPrompt.authenticate(getCancelSignal(), mainExecutor, authenticationCallback)
        }
    }

    private fun notificationPopup(message: String) {
        Toast.makeText(this, message, Toast.LENGTH_SHORT).show()
    }

    private fun getCancelSignal() : CancellationSignal {
        cancelSignal = CancellationSignal()
        cancelSignal?.setOnCancelListener {
            notificationPopup("Authentication was cancelled by user.")
        }
        return cancelSignal as CancellationSignal
    }

    private fun checkCompatability(): Boolean {
        val keyguardManager : KeyguardManager = getSystemService(Context.KEYGUARD_SERVICE) as KeyguardManager

        if (!keyguardManager.isKeyguardSecure) {
            notificationPopup("Fingerprint authentication is not enabled in settings.")
            return false
        }

        if (ActivityCompat.checkSelfPermission(this, android.Manifest.permission.USE_BIOMETRIC) != PackageManager.PERMISSION_GRANTED) {
            notificationPopup("Fingerprint authentication permission not active.")
            return false
        }

        return if (packageManager.hasSystemFeature(PackageManager.FEATURE_FINGERPRINT)) {
            true
        } else true
    }
}