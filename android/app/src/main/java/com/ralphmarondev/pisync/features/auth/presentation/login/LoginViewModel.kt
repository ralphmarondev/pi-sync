package com.ralphmarondev.pisync.features.auth.presentation.login

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ralphmarondev.pisync.features.auth.domain.model.Result
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

class LoginViewModel(

) : ViewModel() {

    private val _username = MutableStateFlow("")
    val username: StateFlow<String> get() = _username

    private val _password = MutableStateFlow("")
    val password: StateFlow<String> get() = _password

    private val _rememberMe = MutableStateFlow(true)
    val rememberMe: StateFlow<Boolean> get() = _rememberMe

    private val _showForgotPasswordDialog = MutableStateFlow(false)
    val showForgotPasswordDialog: StateFlow<Boolean> get() = _showForgotPasswordDialog

    private val _showSetupIpDialog = MutableStateFlow(false)
    val showSetupIpDialog: StateFlow<Boolean> get() = _showSetupIpDialog

    private val _response = MutableStateFlow(Result())
    val response: StateFlow<Result> get() = _response

    private val _passwordHint = MutableStateFlow("")
    val passwordHint = _passwordHint.asStateFlow()

    private fun getPasswordHint() {
        viewModelScope.launch {
        }
    }

    fun onUsernameChange(value: String) {
        _username.value = value
    }

    fun onPasswordChange(value: String) {
        _password.value = value
    }

    fun toggleRememberMe() {

    }

    fun toggleForgotPasswordDialog() {
        getPasswordHint()
        _showForgotPasswordDialog.value = !_showForgotPasswordDialog.value
    }

    fun toggleSetupIpDialog() {
        _showSetupIpDialog.value = !_showSetupIpDialog.value
    }

    fun login() {
        viewModelScope.launch {

        }
    }

    fun saveServerIpAddress(ipAddress: String) {
        viewModelScope.launch {

        }
    }
}