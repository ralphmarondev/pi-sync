package com.ralphmarondev.pisync.navigation

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.ralphmarondev.pisync.core.data.local.preferences.AppPreferences
import com.ralphmarondev.pisync.core.util.LocalThemeState
import com.ralphmarondev.pisync.features.auth.presentation.login.LoginScreen
import com.ralphmarondev.pisync.features.home.presentation.HomeScreen
import com.ralphmarondev.pisync.ui.theme.PiSyncTheme

@Composable
fun AppNavigation(
    preferences: AppPreferences,
    navController: NavHostController = rememberNavController()
) {
    val themeState = LocalThemeState.current
    val startDestination: Any = if (preferences.isFirstLaunch()) {
        Routes.Onboarding
    } else {
        Routes.Login
    }

    PiSyncTheme(
        darkTheme = themeState.darkTheme.value
    ) {
        NavHost(
            navController = navController,
            startDestination = startDestination
        ) {
            composable<Routes.Onboarding> {
                Column(
                    modifier = Modifier
                        .fillMaxSize()
                        .padding(16.dp),
                    horizontalAlignment = Alignment.CenterHorizontally,
                    verticalArrangement = Arrangement.Center
                ) {
                    Text(
                        text = "Onboarding Screen",
                        fontSize = MaterialTheme.typography.titleMedium.fontSize,
                        fontWeight = MaterialTheme.typography.titleMedium.fontWeight,
                        color = MaterialTheme.colorScheme.secondary,
                        textAlign = TextAlign.Center
                    )

                    Button(
                        onClick = {
                            preferences.setFirstLaunch()
                            navController.navigate(Routes.Login) {
                                popUpTo<Routes.Onboarding> { inclusive = true }
                                launchSingleTop = true
                            }
                        }
                    ) {
                        Text(
                            text = "Get Started",
                            fontSize = MaterialTheme.typography.titleMedium.fontSize,
                            fontWeight = MaterialTheme.typography.titleMedium.fontWeight
                        )
                    }
                }
            }
            composable<Routes.Login> {
                LoginScreen(
                    onLoginSuccessful = {
                        navController.navigate(Routes.Home) {
                            popUpTo<Routes.Login> { inclusive = true }
                            launchSingleTop = true
                        }
                    }
                )
            }
            composable<Routes.Home> {
                HomeScreen()
            }
        }
    }
}