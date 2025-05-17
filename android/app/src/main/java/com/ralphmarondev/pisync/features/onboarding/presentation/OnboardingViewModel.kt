package com.ralphmarondev.pisync.features.onboarding.presentation

import androidx.lifecycle.ViewModel
import com.ralphmarondev.pisync.core.data.local.preferences.AppPreferences
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow

class OnboardingViewModel(
    private val preferences: AppPreferences
) : ViewModel() {

    private val _showCompletedDialog = MutableStateFlow(false)
    val showCompletedDialog = _showCompletedDialog.asStateFlow()

    private val _screenContentCount = MutableStateFlow(0)
    val screenContentCount = _screenContentCount.asStateFlow()

    fun showCompletedDialog() {
        _showCompletedDialog.value = true
    }

    fun setOnboardingCompleted() {
        _showCompletedDialog.value = false
        preferences.setFirstLaunch()
    }

    fun incrementScreenContentCount() {
        _screenContentCount.value += 1
    }
}