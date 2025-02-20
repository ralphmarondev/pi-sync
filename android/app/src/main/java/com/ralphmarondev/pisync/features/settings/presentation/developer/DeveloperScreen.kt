package com.ralphmarondev.pisync.features.settings.presentation.developer

import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
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
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun DeveloperScreen(
    navigateBack: () -> Unit
) {
    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Text(
                        text = "Developer"
                    )
                },
                navigationIcon = {
                    IconButton(
                        onClick = navigateBack
                    ) {
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
                .padding(innerPadding)
                .padding(horizontal = 16.dp),
        ) {
            item { Spacer(modifier = Modifier.height(16.dp)) }
            item {
                Text(
                    text = "This project is developed by:",
                    fontSize = 18.sp,
                    fontWeight = FontWeight.W500,
                    color = MaterialTheme.colorScheme.primary
                )
                Text(
                    text = "Ralph Maron Eda",
                    fontSize = 16.sp,
                    fontWeight = FontWeight.W400,
                    color = MaterialTheme.colorScheme.secondary,
                    modifier = Modifier.padding(vertical = 4.dp)
                )
                Text(
                    text = "API, Desktop App, Mobile App Development, UI Design, Data Structure and Algorithm Design. Responsible for Software and Hardware Integration.",
                    fontSize = 16.sp,
                    fontWeight = FontWeight.W300,
                    color = MaterialTheme.colorScheme.tertiary
                )
//                HorizontalDivider(modifier = Modifier.padding(vertical = 8.dp))
//
//                Text(
//                    text = "Contributors:",
//                    fontSize = 18.sp,
//                    fontWeight = FontWeight.W500,
//                    color = MaterialTheme.colorScheme.primary
//                )
                Text(
                    text = "Jack Cabigayan",
                    fontSize = 16.sp,
                    fontWeight = FontWeight.W400,
                    color = MaterialTheme.colorScheme.secondary,
                    modifier = Modifier.padding(vertical = 4.dp)
                )
                Text(
                    text = "Assisted in hardware integration and testing, Contributed to the papers.",
                    fontSize = 16.sp,
                    fontWeight = FontWeight.W300,
                    color = MaterialTheme.colorScheme.tertiary
                )
                Text(
                    text = "Triesha Mae Olunan",
                    fontSize = 16.sp,
                    fontWeight = FontWeight.W400,
                    color = MaterialTheme.colorScheme.secondary,
                    modifier = Modifier.padding(vertical = 4.dp)
                )
                Text(
                    text = "Assisted in hardware integration and testing, Contributed to the papers.",
                    fontSize = 16.sp,
                    fontWeight = FontWeight.W300,
                    color = MaterialTheme.colorScheme.tertiary
                )
                Text(
                    text = "Jezlyn Cabbab",
                    fontSize = 16.sp,
                    fontWeight = FontWeight.W400,
                    color = MaterialTheme.colorScheme.secondary,
                    modifier = Modifier.padding(vertical = 4.dp)
                )
                Text(
                    text = "Assisted in hardware integration and testing, Contributed to the papers.",
                    fontSize = 16.sp,
                    fontWeight = FontWeight.W300,
                    color = MaterialTheme.colorScheme.tertiary
                )
                HorizontalDivider(modifier = Modifier.padding(vertical = 8.dp))
                Text(
                    text = "Special Thanks:",
                    fontSize = 18.sp,
                    fontWeight = FontWeight.W500,
                    color = MaterialTheme.colorScheme.primary
                )
                Text(
                    text = "Engr. Jerome Paul Viador",
                    fontSize = 16.sp,
                    fontWeight = FontWeight.W400,
                    color = MaterialTheme.colorScheme.secondary,
                    modifier = Modifier.padding(vertical = 4.dp)
                )
                Text(
                    text = "Thesis Adviser and Project Guidance",
                    fontSize = 16.sp,
                    fontWeight = FontWeight.W300,
                    color = MaterialTheme.colorScheme.tertiary
                )
            }
            item { Spacer(modifier = Modifier.height(100.dp)) }
        }
    }
}