package com.ralphmarondev.pisync.features.setup.presentation

import androidx.lifecycle.ViewModel
import com.ralphmarondev.pisync.MyApp
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow

class SetupViewModel : ViewModel() {
    private val preferences = MyApp.preferences

    private val _ipAddress = MutableStateFlow(preferences.getIpAddress().toString())
    val ipAddress: StateFlow<String> get() = _ipAddress

    fun onIpAddressChange(value: String) {
        _ipAddress.value = value
    }

    fun saveIpAddress() {
        if (_ipAddress.value.trim().isNotEmpty()) {
            preferences.saveIpAddress(value = _ipAddress.value)
        }
    }
}