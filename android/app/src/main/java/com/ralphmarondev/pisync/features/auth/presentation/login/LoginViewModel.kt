package com.ralphmarondev.pisync.features.auth.presentation.login

import android.util.Log
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ralphmarondev.pisync.core.data.local.preferences.AppPreferences
import com.ralphmarondev.pisync.core.domain.model.Result
import com.ralphmarondev.pisync.features.auth.domain.usecases.ForgotPasswordUseCase
import com.ralphmarondev.pisync.features.auth.domain.usecases.LoginUseCase
import com.ralphmarondev.pisync.features.overview.domain.usecases.GetUserDetailByUsernameUseCase
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

class LoginViewModel(
    private val preferences: AppPreferences,
    private val loginUseCase: LoginUseCase,
    private val forgotPasswordUseCase: ForgotPasswordUseCase,
    private val getUserDetailByUsernameUseCase: GetUserDetailByUsernameUseCase
) : ViewModel() {

    private val _username = MutableStateFlow(preferences.getRememberedUsername() ?: "")
    val username = _username.asStateFlow()

    private val _password = MutableStateFlow(preferences.getRememberedPassword() ?: "")
    val password = _password.asStateFlow()

    private val _rememberMe = MutableStateFlow(preferences.isRememberMeChecked())
    val rememberMe = _rememberMe.asStateFlow()

    private val _showForgotPasswordDialog = MutableStateFlow(false)
    val showForgotPasswordDialog = _showForgotPasswordDialog.asStateFlow()

    private val _showSetupIpDialog = MutableStateFlow(false)
    val showSetupIpDialog = _showSetupIpDialog.asStateFlow()

    private val _response = MutableStateFlow(Result())
    val response = _response.asStateFlow()

    private val _passwordHint = MutableStateFlow("")
    val passwordHint = _passwordHint.asStateFlow()


    fun onUsernameChange(value: String) {
        _username.value = value
    }

    fun onPasswordChange(value: String) {
        _password.value = value
    }

    fun toggleRememberMe() {
        _rememberMe.value = !_rememberMe.value
        preferences.setRememberMe()
    }

    fun toggleForgotPasswordDialog() {
        viewModelScope.launch {
            _showForgotPasswordDialog.value = !_showForgotPasswordDialog.value
            try {
                val username = _username.value.trim()

                if (username.isEmpty()) {
                    _passwordHint.value = "Can't retrieve password hint. No username provided."
                    return@launch
                }
                val result = forgotPasswordUseCase(username)
                _passwordHint.value = result
            } catch (e: Exception) {
                Log.e("App", "Error getting password hint: ${e.message}")
                _passwordHint.value = "No hint available."
            }
        }
    }

    fun toggleSetupIpDialog() {
        _showSetupIpDialog.value = !_showSetupIpDialog.value
    }

    fun login() {
        viewModelScope.launch {
            val username = _username.value.trim()
            val password = _password.value.trim()

            if (username.isEmpty()) {
                _response.value = Result(
                    success = false,
                    message = "Username cannot be empty"
                )
                return@launch
            }
            if (password.isEmpty()) {
                _response.value = Result(
                    success = false,
                    message = "Password cannot be empty"
                )
                return@launch
            }

            try {
                if (loginUseCase(username, password)) {
                    val userDetail = getUserDetailByUsernameUseCase(username)
                    if (userDetail.isSuperUser) {
                        _response.value = Result(
                            success = false,
                            message = "Login failed. You are trying to login with a superuser account."
                        )
                        return@launch
                    }

                    _response.value = Result(
                        success = true,
                        message = "Login successful"
                    )
                    if (_rememberMe.value) {
                        preferences.setUsernameToRemember(username)
                        preferences.setPasswordToRemember(password)
                    }
                    preferences.setCurrentUser(username)
                } else {
                    _response.value = Result(
                        success = false,
                        message = "Invalid credentials. Please try again."
                    )
                }
            } catch (e: Exception) {
                _response.value = Result(
                    success = false,
                    message = "Invalid credentials. Please try again."
                )
            }
        }
    }

    fun saveServerIpAddress(ipAddress: String) {
        viewModelScope.launch {
            Log.d("App", "New ip address: $ipAddress")
        }
    }
}