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
        if (ipAddress != null) {
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
}