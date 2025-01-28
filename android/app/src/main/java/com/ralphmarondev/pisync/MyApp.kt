package com.ralphmarondev.pisync

import android.app.Application
import android.util.Log
import android.widget.Toast
import com.ralphmarondev.pisync.core.data.network.RetrofitInstance
import com.ralphmarondev.pisync.core.data.preferences.AppPreferences

class MyApp : Application() {
    companion object {
        lateinit var preferences: AppPreferences
            private set
    }

    override fun onCreate() {
        super.onCreate()
        preferences = AppPreferences(applicationContext)

        val ipAddress = preferences.getIpAddress()
        if (ipAddress != null && isValidIpAddress(ipAddress)) {
            val baseUrl = "http://$ipAddress:8000/api/"
            RetrofitInstance.initialize(baseUrl)
            Log.d("MyApp", "Retrofit initialized with baseUrl: $baseUrl")
        } else {
            Log.d("MyApp", "No ip address found. Some functionality might not work.")
            Toast.makeText(
                applicationContext,
                "No ip address found. Some functionality might not work.",
                Toast.LENGTH_SHORT
            ).show()
        }
    }

    private fun isValidIpAddress(ip: String): Boolean {
        val regex =
            """^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$""".toRegex()
        return regex.matches(ip)
    }
}