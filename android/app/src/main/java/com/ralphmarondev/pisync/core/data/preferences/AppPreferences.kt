package com.ralphmarondev.pisync.core.data.preferences

import android.content.Context
import android.content.SharedPreferences

class AppPreferences(context: Context) {
    companion object {
        private const val PREFERENCES_NAME = "pisync_preferences"
        private const val FIRST_LAUNCH = "first_launch"
        private const val DARK_THEME = "dark_theme"
        private const val CURRENT_USER = "current_user"
    }

    private val sharedPreferences: SharedPreferences = context.getSharedPreferences(
        PREFERENCES_NAME, Context.MODE_PRIVATE
    )

    fun isFirstLaunch(): Boolean {
        return sharedPreferences.getBoolean(FIRST_LAUNCH, true)
    }

    fun setFirstLaunch() {
        sharedPreferences.edit().putBoolean(FIRST_LAUNCH, false).apply()
    }

    fun isDarkTheme(): Boolean {
        return sharedPreferences.getBoolean(DARK_THEME, false)
    }

    fun toggleDarkTheme() {
        sharedPreferences.edit().putBoolean(DARK_THEME, !isDarkTheme()).apply()
    }

    fun setCurrentUser(value: String) {
        sharedPreferences.edit().putString(CURRENT_USER, value).apply()
    }

    fun getCurrentUser(): String {
        return sharedPreferences.getString(CURRENT_USER, "no_user")!!
    }
}