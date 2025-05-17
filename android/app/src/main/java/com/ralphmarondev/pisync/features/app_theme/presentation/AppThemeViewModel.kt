package com.ralphmarondev.pisync.features.app_theme.presentation

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ralphmarondev.pisync.core.data.local.preferences.AppPreferences
import com.ralphmarondev.pisync.core.util.AppColorTheme
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

class AppThemeViewModel(
    private val preferences: AppPreferences
) : ViewModel() {

    private val _currentThemeColor = MutableStateFlow("")
    val currentThemeColor = _currentThemeColor.asStateFlow()

    init {
        viewModelScope.launch {
            _currentThemeColor.value = preferences.getThemeColor() ?: AppColorTheme.PURPLE
        }
    }

    fun updateThemeColor(color: String) {
        viewModelScope.launch {
            preferences.setThemeColor(color)
            _currentThemeColor.value = color
        }
    }
}