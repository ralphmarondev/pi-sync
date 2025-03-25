package com.ralphmarondev.pisync

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.core.splashscreen.SplashScreen.Companion.installSplashScreen
import com.ralphmarondev.pisync.core.data.local.preferences.AppPreferences
import com.ralphmarondev.pisync.core.util.ThemeProvider
import com.ralphmarondev.pisync.core.util.ThemeState
import com.ralphmarondev.pisync.navigation.AppNavigation
import org.koin.android.ext.android.inject

class MainActivity : ComponentActivity() {

    private val preferences: AppPreferences by inject()
    private val themeState: ThemeState by inject()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        installSplashScreen()
        enableEdgeToEdge()

        setContent {
            ThemeProvider(themeState = themeState) {
                AppNavigation(preferences)
            }
        }
    }
}