package com.ralphmarondev.pisync.features.auth.presentation

import androidx.lifecycle.ViewModel
import com.ralphmarondev.pisync.MyApp
import com.ralphmarondev.pisync.core.data.model.Result
import com.ralphmarondev.pisync.features.auth.data.repository.AuthRepositoryImpl
import com.ralphmarondev.pisync.features.auth.domain.usecases.LoginUseCase
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow

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

    private val _response = MutableStateFlow(Result(success = false, message = ""))

    init {
        if (preferences.isRememberMeChecked()) {
            val savedUsername = preferences.getCurrentUserUsername()
            val savedPassword = preferences.getCurrentUserPassword()

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

    fun login(): Result {
        if (_username.value.trim().isBlank() || _password.value.trim().isBlank()) {
            return Result(success = false, message = "Username or password cannot be empty!")
        }

        if (_rememberMe.value) {
            preferences.setCurrentUserUsername(_username.value.trim())
            preferences.setCurrentUserPassword(_password.value.trim())
        }

//        viewModelScope.launch {
//            val loginRequest = LoginRequest(_username.value.trim(), _password.value.trim())
//            _response.value = loginUseCase.login(loginRequest)
//        }

//        return _response.value

        return Result(
            success = true,
            message = "Login successful."
        )
    }
}