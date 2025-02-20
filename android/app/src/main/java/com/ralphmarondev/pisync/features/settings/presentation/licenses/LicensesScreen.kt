package com.ralphmarondev.pisync.features.settings.presentation.licenses

import android.content.Intent
import android.net.Uri
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.outlined.ArrowBackIosNew
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun LicensesScreen(
    navigateBack: () -> Unit
) {
    val context = LocalContext.current
    val licenses = listOf(
        License(
            name = "Android Studio",
            license = "Apache License 2.0",
            link = "https://www.apache.org/licenses/LICENSE-2.0"
        ),
        License(
            name = "Kotlin",
            license = "Apache License 2.0",
            link = "https://www.apache.org/licenses/LICENSE-2.0"
        ),
        License(
            name = "Jetpack Compose",
            license = "Apache License 2.0",
            link = "https://www.apache.org/licenses/LICENSE-2.0"
        ),
        License(
            name = "Material3 (Material Design)",
            license = "Apache License 2.0",
            link = "https://www.apache.org/licenses/LICENSE-2.0"
        ),
        License(
            name = "Coil",
            license = "MIT License",
            link = "https://opensource.org/licenses/MIT"
        ),
        License(
            name = "Retrofit",
            license = "Apache License 2.0",
            link = "https://www.apache.org/licenses/LICENSE-2.0"
        ),
        License(
            name = "Django REST Framework",
            license = "BSD License",
            link = "https://opensource.org/licenses/BSD-3-Clause"
        ),
        License(
            name = "Python",
            license = "Python Software Foundation License",
            link = "https://opensource.org/licenses/Python-2.0"
        )
    )

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Text(
                        text = "Licenses"
                    )
                },
                navigationIcon = {
                    IconButton(onClick = navigateBack) {
                        Icon(
                            imageVector = Icons.Outlined.ArrowBackIosNew,
                            contentDescription = "Navigate back"
                        )
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(
                    containerColor = MaterialTheme.colorScheme.primary,
                    titleContentColor = MaterialTheme.colorScheme.onPrimary,
                    navigationIconContentColor = MaterialTheme.colorScheme.onPrimary
                )
            )
        }
    ) { innerPadding ->
        LazyColumn(
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding),
            contentPadding = PaddingValues(horizontal = 16.dp)
        ) {
            item { Spacer(modifier = Modifier.height(16.dp)) }
            items(licenses) { license ->
                Text(
                    text = license.name,
                    fontSize = 18.sp,
                    fontWeight = FontWeight.W500,
                    color = MaterialTheme.colorScheme.primary
                )
                Text(
                    text = license.license,
                    fontSize = 16.sp,
                    fontWeight = FontWeight.W400,
                    color = MaterialTheme.colorScheme.secondary,
                    modifier = Modifier.padding(vertical = 4.dp)
                )
                Text(
                    text = license.link,
                    fontSize = 16.sp,
                    fontWeight = FontWeight.W300,
                    color = MaterialTheme.colorScheme.tertiary,
                    modifier = Modifier
                        .clickable {
                            val intent = Intent(
                                Intent.ACTION_VIEW,
                                Uri.parse(license.link)
                            )
                            context.startActivity(intent)
                        }
                )
                HorizontalDivider(modifier = Modifier.padding(vertical = 8.dp))
            }
            item { Spacer(modifier = Modifier.height(100.dp)) }
        }
    }
}

private data class License(
    val name: String,
    val license: String,
    val link: String
)