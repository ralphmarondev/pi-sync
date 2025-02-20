package com.ralphmarondev.pisync.features.auth.presentation

import android.util.Log
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ralphmarondev.pisync.MyApp
import com.ralphmarondev.pisync.core.domain.Result
import com.ralphmarondev.pisync.features.auth.data.repository.AuthRepositoryImpl
import com.ralphmarondev.pisync.features.auth.domain.model.User
import com.ralphmarondev.pisync.features.auth.domain.usecases.LoginUseCase
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch

class AuthViewModel : ViewModel() {
    private val preferences = MyApp.preferences
    private val repository = AuthRepositoryImpl(preferences)
    private val loginUseCase = LoginUseCase(repository)

    private val _username = MutableStateFlow("")
    val username: StateFlow<String> get() = _username

    private val _password = MutableStateFlow("")
    val password: StateFlow<String> get() = _password

    private val _rememberMe = MutableStateFlow(preferences.isRememberMeChecked())
    val rememberMe: StateFlow<Boolean> get() = _rememberMe

    private val _showForgotPasswordDialog = MutableStateFlow(false)
    val showForgotPasswordDialog: StateFlow<Boolean> get() = _showForgotPasswordDialog

    private val _showSetupIpDialog = MutableStateFlow(false)
    val showSetupIpDialog: StateFlow<Boolean> get() = _showSetupIpDialog

    private val _response = MutableStateFlow<Result?>(null)
    val response: StateFlow<Result?> get() = _response

    init {
        if (preferences.isRememberMeChecked()) {
            val savedUsername = preferences.getRememberedUsername()
            val savedPassword = preferences.getRememberedPassword()

            _username.value = when (savedUsername != "no_user") {
                true -> savedUsername
                false -> ""
            }
            _password.value = when (savedPassword != "no_user") {
                true -> savedPassword
                false -> ""
            }
        }
    }

    fun onUsernameChange(value: String) {
        _username.value = value
    }

    fun onPasswordChange(value: String) {
        _password.value = value
    }

    fun toggleRememberMe() {
        _rememberMe.value = !_rememberMe.value
        preferences.toggleRememberMe()
    }

    fun toggleForgotPasswordDialog() {
        _showForgotPasswordDialog.value = !_showForgotPasswordDialog.value
    }

    fun toggleSetupIpDialog() {
        _showSetupIpDialog.value = !_showSetupIpDialog.value
    }

    fun login() {
        if (_username.value.trim().isBlank() || _password.value.trim().isBlank()) {
            _response.value = Result(
                success = false,
                message = "Username or password cannot be empty!"
            )
        }

        if (_rememberMe.value) {
            preferences.setUsernameToRemember(_username.value.trim())
            preferences.setPasswordToRemember(_password.value.trim())
        }

        viewModelScope.launch {
            val user = User(
                username = _username.value.trim(),
                password = _password.value.trim()
            )
            _response.value = loginUseCase.login(user)

            if (_response.value!!.success == true) {
                preferences.setActiveUserUsername(_username.value.trim())
            }
        }

        Log.d("Auth", "Setting active user: ${_username.value.trim()}")
        preferences.setActiveUserUsername(_username.value.trim())
    }

    fun saveServerIpAddress(ipAddress: String) {
        viewModelScope.launch {
            try {
                preferences.saveIpAddress(ipAddress)
                Log.d("Auth", "IP address saved. IP: `$ipAddress`")
            } catch (e: Exception) {
                Log.e("Auth", "Error saving IP address: ${e.message}")
            }
        }
    }
}