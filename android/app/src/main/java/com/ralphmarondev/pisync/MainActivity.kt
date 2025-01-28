package com.ralphmarondev.pisync

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import com.ralphmarondev.pisync.navigation.AppNavigation
import com.ralphmarondev.pisync.ui.theme.PiSyncTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            val preferences = MyApp.preferences
            var darkTheme by remember { mutableStateOf(preferences.isDarkTheme()) }

            PiSyncTheme(darkTheme = darkTheme) {
                AppNavigation(
                    darkTheme = darkTheme,
                    toggleDarkTheme = {
                        darkTheme = !darkTheme
                        preferences.toggleDarkTheme()
                    },
                    preferences = preferences
                )
            }
        }
    }
}