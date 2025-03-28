package com.ralphmarondev.pisync.core.data.local.preferences

import android.content.Context
import android.content.SharedPreferences
import androidx.core.content.edit

class AppPreferences(context: Context) {
    companion object {
        private const val PREFERENCES_NAME = "pisync_preferences"
        private const val FIRST_LAUNCH = "first_launch"
        private const val DARK_THEME = "dark_theme"
        private const val REMEMBER_ME = "remember_me"
        private const val SAVED_USERNAME = "saved_username"
        private const val SAVED_PASSWORD = "saved_password"
        private const val IP_ADDRESS = "ip_address"
        private const val CURRENT_USERNAME = "current_username"
    }

    private val sharedPreferences: SharedPreferences = context.getSharedPreferences(
        PREFERENCES_NAME, Context.MODE_PRIVATE
    )

    fun saveIpAddress(value: String) {
        sharedPreferences.edit { putString(IP_ADDRESS, value) }
    }

    fun getIpAddress(): String? {
        return sharedPreferences.getString(IP_ADDRESS, null)
    }

    fun isFirstLaunch(): Boolean {
        return sharedPreferences.getBoolean(FIRST_LAUNCH, true)
    }

    fun setFirstLaunch() {
        sharedPreferences.edit { putBoolean(FIRST_LAUNCH, false) }
    }

    fun isDarkTheme(): Boolean {
        return sharedPreferences.getBoolean(DARK_THEME, false)
    }

    fun setDarkTheme() {
        sharedPreferences.edit { putBoolean(DARK_THEME, !isDarkTheme()) }
    }

    fun isRememberMeChecked(): Boolean {
        return sharedPreferences.getBoolean(REMEMBER_ME, true)
    }

    fun setRememberMe() {
        sharedPreferences.edit { putBoolean(REMEMBER_ME, !isRememberMeChecked()) }
    }

    fun setUsernameToRemember(value: String) {
        sharedPreferences.edit { putString(SAVED_USERNAME, value) }
    }

    fun getRememberedUsername(): String? {
        return sharedPreferences.getString(SAVED_USERNAME, null)
    }

    fun setPasswordToRemember(value: String) {
        sharedPreferences.edit { putString(SAVED_PASSWORD, value) }
    }

    fun getRememberedPassword(): String? {
        return sharedPreferences.getString(SAVED_PASSWORD, null)
    }

    fun setCurrentUser(value: String) {
        sharedPreferences.edit { putString(CURRENT_USERNAME, value) }
    }

    fun getCurrentUser(): String? {
        return sharedPreferences.getString(CURRENT_USERNAME, null)
    }
}