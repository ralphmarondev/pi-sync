package com.ralphmarondev.pisync.core.data.preferences

import android.content.Context
import android.content.SharedPreferences

class AppPreferences(context: Context) {
    companion object {
        private const val PREFERENCES_NAME = "pisync_preferences"
        private const val FIRST_LAUNCH = "first_launch"
        private const val DARK_THEME = "dark_theme"
        private const val REMEMBER_ME = "remember_me"
        private const val CURRENT_USER_USERNAME = "current_user_username"
        private const val CURRENT_USER_PASSWORD = "current_user_password"
        private const val IP_ADDRESS = "ip_address"
    }

    private val sharedPreferences: SharedPreferences = context.getSharedPreferences(
        PREFERENCES_NAME, Context.MODE_PRIVATE
    )

    fun saveIpAddress(value: String) {
        sharedPreferences.edit().putString(IP_ADDRESS, value).apply()
    }

    fun getIpAddress(): String? {
        return sharedPreferences.getString(IP_ADDRESS, null)
    }

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

    fun toggleRememberMe() {
        sharedPreferences.edit().putBoolean(REMEMBER_ME, !isRememberMeChecked()).apply()
    }

    fun isRememberMeChecked(): Boolean {
        return sharedPreferences.getBoolean(REMEMBER_ME, false)
    }

    fun setCurrentUserUsername(value: String) {
        sharedPreferences.edit().putString(CURRENT_USER_USERNAME, value).apply()
    }

    fun getCurrentUserUsername(): String {
        return sharedPreferences.getString(CURRENT_USER_USERNAME, "no_user")!!
    }

    fun setCurrentUserPassword(value: String) {
        sharedPreferences.edit().putString(CURRENT_USER_PASSWORD, value).apply()
    }

    fun getCurrentUserPassword(): String {
        return sharedPreferences.getString(CURRENT_USER_PASSWORD, "no_user")!!
    }
}