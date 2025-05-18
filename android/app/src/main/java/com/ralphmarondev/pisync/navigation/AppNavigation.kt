package com.ralphmarondev.pisync.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.ralphmarondev.pisync.core.data.local.preferences.AppPreferences
import com.ralphmarondev.pisync.core.util.LocalThemeState
import com.ralphmarondev.pisync.features.about.presentation.AboutScreen
import com.ralphmarondev.pisync.features.app_theme.presentation.AppThemeScreen
import com.ralphmarondev.pisync.features.auth.presentation.login.LoginScreen
import com.ralphmarondev.pisync.features.home.presentation.HomeScreen
import com.ralphmarondev.pisync.features.onboarding.presentation.OnboardingScreen
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
        darkTheme = themeState.darkTheme.value,
        preferences = preferences,
        dynamicColor = false,
        content = {
            NavHost(
                navController = navController,
                startDestination = startDestination
            ) {
                composable<Routes.Onboarding> {
                    OnboardingScreen(
                        onboardingCompleted = {
                            navController.navigate(Routes.Login) {
                                popUpTo(0) { inclusive = true }
                                launchSingleTop = true
                            }
                        }
                    )
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
                    HomeScreen(
                        onLogout = {
                            navController.navigate(Routes.Login) {
                                popUpTo(0) { inclusive = true }
                                launchSingleTop = true
                            }
                        },
                        navigateToAbout = {
                            navController.navigate(Routes.About) {
                                launchSingleTop = true
                            }
                        },
                        navigateToAppTheme = {
                            navController.navigate(Routes.AppTheme) {
                                launchSingleTop = true
                            }
                        }
                    )
                }
                composable<Routes.About> {
                    AboutScreen(
                        navigateBack = {
                            navController.navigateUp()
                        }
                    )
                }
                composable<Routes.AppTheme> {
                    AppThemeScreen(
                        navigateBack = {
                            navController.navigateUp()
                        }
                    )
                }
            }
        }
    )
}